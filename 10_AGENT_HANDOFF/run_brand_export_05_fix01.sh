#!/usr/bin/env bash
# BRAND-EXPORT-05-FIX-01 runner. Started once by the bootstrap block; stops at the first failure.
# Never resets, deletes, amends, tags, or pushes to main. On failure the log stays at /tmp/ycn05fix_run.log.
set -euo pipefail
set -o noclobber

REPO=/home/ycn-labs/Desktop/YCN_LABS_MASTER/01_CURRENT_PROJECT/YCN_LABS_BRAND_LIBRARY
EXP=10_AGENT_HANDOFF/export_png_kit_v2.py
RUNNER=10_AGENT_HANDOFF/run_brand_export_05_fix01.sh
DEVREC=13_AI_REPORTS/AGY_DEVIATIONS_BRAND-EXPORT-05.md
LOG=08_QUALITY_AND_EVIDENCE/BRAND-EXPORT-05/FIX-01_RUN_LOG.txt
INV=14_CONTINUITY/SHA256SUMS.txt
OLD=234846841534cd97961fa8555051dcf73ef086dd
MAIN=386f9794736efca8a6bd03ffd774553790857dc8
WIP=refs/heads/wip/brand-export-05
S=/tmp/ycn05fix
R1="${S}_run1"
R2="${S}_run2"
SECRET_RE='BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|(password|passwd|secret|api[_-]?key)[[:space:]]*[:=]'
cd "$REPO"
PY="$(command -v python3)"

die() { echo "STOP: $*"; exit 1; }
step() { echo; echo "=== $* ==="; }
scan() {
  local rc=0
  grep -lE "$SECRET_RE" -- "$@" || rc=$?
  case "$rc" in
    1) echo "scan: no secret-like pattern in $*" ;;
    0) die "secret-like pattern in the file(s) listed above" ;;
    *) die "scan error (grep exit $rc)" ;;
  esac
}
remote_is() { [ "$(git ls-remote origin "$1" | cut -f1)" = "$2" ] || die "remote $1 is not $2"; }

for p in "$R1" "$R2" "${S}_h1.txt" "${S}_h2.txt" "${S}_list.txt" "${S}_protected.sha256" "${S}_changes.txt" "${S}_run.log" "$LOG"; do
  { [ ! -e "$p" ] && [ ! -L "$p" ]; } || die "path already exists: $p"
done

main() {
  step "0 identity and starting state"
  date -Iseconds
  echo "interpreter: $PY"
  "$PY" -B -c 'import sys, zlib, PIL; print(sys.version); print("Pillow", PIL.__version__); print("zlib", zlib.ZLIB_RUNTIME_VERSION)'
  "$PY" -B -c 'import sys, PIL; sys.exit(0 if sys.version_info[:2] == (3, 12) and PIL.__version__ == "12.2.0" else 1)' || die "need Python 3.12 with Pillow 12.2.0"
  [ "$(git rev-parse --abbrev-ref HEAD)" = main ] || die "local branch is not main"
  [ "$(git rev-parse HEAD)" = "$OLD" ] || die "HEAD is not $OLD"
  [ "$(git rev-parse HEAD^)" = "$MAIN" ] || die "parent is not $MAIN"
  remote_is refs/heads/main "$MAIN"
  remote_is "$WIP" "$OLD"
  expected=$'?? 10_AGENT_HANDOFF/export_png_kit_v2.py\n?? 10_AGENT_HANDOFF/run_brand_export_05_fix01.sh\n?? 13_AI_REPORTS/AGY_DEVIATIONS_BRAND-EXPORT-05.md'
  actual="$(git status --porcelain --untracked-files=all)"
  echo "$actual"
  [ "$actual" = "$expected" ] || die "working tree is not exactly the three new FIX-01 files"
  sha256sum "$EXP" "$RUNNER" "$DEVREC"

  step "1 baseline integrity"
  [ "$(wc -l < "$INV")" -eq 118 ] || die "live inventory is not 118 entries"
  sha256sum -c "$INV"
  printf '%s\n' \
    "0ceebe4ccf81c478b8b2b2b6674f98ccc4dc93308c8a0e053243984c3a2c2be3  01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K__6675x5195.png" \
    "8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943  01_IMMUTABLE_SOURCE/Main_YCN_LABS_logo_black_8K.png" \
    "85808a7d15646a4847f75612eda95ddda09c9b51c4177f46e0b6814225a07784  11_HISTORICAL_ASSETS/masters/ycn-logo-dark-transparent-MASTER.png" \
    "416de4b7c83a051cf9d11c3e4c88a36690b8be248ef5edb81f7a350af72b28a9  11_HISTORICAL_ASSETS/masters/ycn-logo-light-transparent-MASTER.png" \
    > "${S}_protected.sha256"
  sha256sum -c "${S}_protected.sha256"

  step "2 allowlist: the 28 targets must equal their committed versions in $OLD"
  "$PY" -B "$EXP" list > "${S}_list.txt"
  [ "$(wc -l < "${S}_list.txt")" -eq 28 ] || die "allowlist is not 28 paths"
  while IFS= read -r rel; do
    { [ -f "$rel" ] && [ ! -L "$rel" ]; } || die "not a regular file: $rel"
    git cat-file -e "$OLD:$rel" || die "not in $OLD: $rel"
    [ "$(git hash-object -- "$rel")" = "$(git rev-parse "$OLD:$rel")" ] || die "working file differs from $OLD: $rel"
  done < "${S}_list.txt"
  echo "allowlist: 28 targets identical to $OLD"

  step "3 two independent builds in /tmp"
  "$PY" -B "$EXP" build --repo . --out "$R1"
  "$PY" -B "$EXP" build --repo . --out "$R2"
  (cd "$R1" && find . -type f | LC_ALL=C sort | xargs sha256sum) > "${S}_h1.txt"
  (cd "$R2" && find . -type f | LC_ALL=C sort | xargs sha256sum) > "${S}_h2.txt"
  diff "${S}_h1.txt" "${S}_h2.txt" || die "the two builds differ"
  diff "${S}_list.txt" <(cd "$R1" && find . -type f | LC_ALL=C sort | sed 's|^\./||') || die "build file set differs from the allowlist"
  cat "${S}_h1.txt"

  step "4 verify the build; compare with the PNGs stored in $OLD"
  "$PY" -B "$EXP" verify --repo . --out "$R1"
  "$PY" -B "$EXP" compare-old --repo . --out "$R1"

  step "5 replace exactly the 28 allowlisted files"
  while IFS= read -r rel; do
    cp -- "$R1/$rel" "$rel"
  done < "${S}_list.txt"
  sha256sum -c "${S}_h1.txt"
  "$PY" -B "$EXP" verify --repo . --out .

  step "6 live inventory: update 28 entries, append 3"
  "$PY" -B - <<'PYEOF'
import hashlib
from pathlib import Path
inv = Path("14_CONTINUITY/SHA256SUMS.txt")
lines = inv.read_text(encoding="utf-8").splitlines()
changed = set(Path("/tmp/ycn05fix_list.txt").read_text(encoding="utf-8").split())
new = ["10_AGENT_HANDOFF/export_png_kit_v2.py", "10_AGENT_HANDOFF/run_brand_export_05_fix01.sh",
       "13_AI_REPORTS/AGY_DEVIATIONS_BRAND-EXPORT-05.md"]
def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
out, updated = [], 0
for line in lines:
    path = line.split("  ", 1)[1]
    if path in changed:
        out.append(f"{digest(path)}  {path}")
        updated += 1
    else:
        out.append(line)
listed = {line.split("  ", 1)[1] for line in lines}
assert len(lines) == 118 and updated == 28 and not listed.intersection(new), (len(lines), updated)
out += [f"{digest(p)}  {p}" for p in new]
inv.write_text("\n".join(out) + "\n", encoding="utf-8")
print("inventory entries:", len(out))
PYEOF
  [ "$(wc -l < "$INV")" -eq 121 ] || die "live inventory is not 121 entries"
  sha256sum -c "$INV"
  git diff --numstat -- "$INV"
  sha256sum -c "${S}_protected.sha256"

  step "7 public-content scan"
  scan "$EXP" "$RUNNER" "$DEVREC" 05_EXPORTS/MANIFEST_BRAND-EXPORT-05.json 05_EXPORTS/SHA256SUMS_BRAND-EXPORT-05.txt

  step "8 stage and compare with the exact allowlist"
  git add -- $(cat "${S}_list.txt") "$EXP" "$RUNNER" "$DEVREC" "$INV"
  { while IFS= read -r p; do printf 'M\t%s\n' "$p"; done < "${S}_list.txt"
    printf 'M\t%s\n' "$INV"
    printf 'A\t%s\n' "$EXP" "$RUNNER" "$DEVREC"; } | LC_ALL=C sort > "${S}_changes.txt"
  diff "${S}_changes.txt" <(git diff --cached --name-status | LC_ALL=C sort) || die "staged paths differ from the allowlist"
  echo "staged: 29 modified + 3 added, exactly as allowlisted"
  echo "build-and-verification log ends here"
}

main 2>&1 | tee "${S}_run.log"

step "F1 freeze the log (nothing below is written to it)"
scan "${S}_run.log"
{ [ ! -e "$LOG" ] && [ ! -L "$LOG" ]; } || die "log destination exists"
cp -- "${S}_run.log" "$LOG"
cmp -- "${S}_run.log" "$LOG" || die "log copy differs"
rc=0
grep -qF "  $LOG" "$INV" || rc=$?
[ "$rc" -eq 1 ] || die "log already listed in the inventory, or grep error"
sha256sum -- "$LOG" >> "$INV"
[ "$(wc -l < "$INV")" -eq 122 ] || die "live inventory is not 122 entries"
sha256sum -c --quiet "$INV" || die "inventory check failed"
echo "inventory: 122 entries, all OK"
sha256sum -c --quiet "${S}_protected.sha256" || die "protected sources changed"

step "F2 final staging checks"
scan "$EXP" "$RUNNER" "$DEVREC" "$LOG"
git add -- "$LOG" "$INV"
diff <({ cat "${S}_changes.txt"; printf 'A\t%s\n' "$LOG"; } | LC_ALL=C sort) <(git diff --cached --name-status | LC_ALL=C sort) || die "staged paths differ from the allowlist"
git -c core.whitespace=cr-at-eol diff --cached --check || die "whitespace check failed"
[ -z "$(git status --porcelain --untracked-files=all | grep -v '^[AM]  ')" ] || die "unstaged or untracked changes remain"
git diff --cached --name-only | while IFS= read -r f; do
  [ "$(stat -c %s -- "$f")" -lt 26214400 ] || die "file over 25 MB: $f"
done
echo "staged: 29 modified + 4 added; whitespace clean; all under 25 MB"

step "F3 commit and verify"
remote_is refs/heads/main "$MAIN"
remote_is "$WIP" "$OLD"
git commit -q -m "brand-export-05 fix-01: master cHRM kept in all PNGs; non-clipping proof; complete manifest; exporter v2; deviations record; run log"
NEW="$(git rev-parse HEAD)"
[ "$(git rev-parse HEAD^)" = "$OLD" ] || die "new commit parent is not $OLD"
[ "$(git rev-list --count "$OLD..HEAD")" -eq 1 ] || die "not exactly one new commit"
diff <({ cat "${S}_changes.txt"; printf 'A\t%s\n' "$LOG"; } | LC_ALL=C sort) <(git diff --name-status "$OLD" "$NEW" | LC_ALL=C sort) || die "committed paths differ from the allowlist"
[ -z "$(git status --porcelain --untracked-files=all)" ] || die "working tree not clean after commit"
sha256sum -c --quiet "$INV" || die "inventory check failed after commit"
sha256sum -c --quiet "${S}_protected.sha256" || die "protected sources changed"

step "F4 publish to the WIP branch only"
remote_is refs/heads/main "$MAIN"
remote_is "$WIP" "$OLD"
git -c push.followTags=false push origin "$NEW:$WIP"
remote_is "$WIP" "$NEW"
remote_is refs/heads/main "$MAIN"
echo "FIX-01 DONE: $NEW on wip/brand-export-05 (parent $OLD); main still $MAIN; inventory 122 OK. STOP."
