#!/usr/bin/env python3
"""Read-only hash + format check of owner supplied YCN Labs source."""
import hashlib, struct, pathlib, sys
EXPECTED_SHA = "8b982547e2c0b5990b710941d29ada29cadfcf6142278998ddf10ae0ace1d943"
EXPECTED_SIZE = 3158172
EXPECTED_DIMS = (2048,1593)

def main(path):
    p=pathlib.Path(path)
    b=p.read_bytes()
    h=hashlib.sha256(b).hexdigest()
    if b[:8] != b"\x89PNG\r\n\x1a\n": raise SystemExit('Not a PNG file')
    width,height,depth,color,compression,filter_method,interlace = struct.unpack('>IIBBBBB',b[16:29])
    print(f'FILE: {p}\nSHA256: {h}\nBYTES: {len(b)}\nSIZE: {width}x{height}\nBIT_DEPTH: {depth}\nPNG_COLOR_TYPE: {color}')
    assert h==EXPECTED_SHA, 'ERROR: NOT IDENTICAL TO OWNER SOURCE'
    assert len(b)==EXPECTED_SIZE and (width,height)==EXPECTED_DIMS and depth==8 and color==6, 'Metadata mismatch'
    print('PASS: file bytes exactly match Owner-supplied PNG')
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python verify_original.py /path/to/file.png')
    main(sys.argv[1])
