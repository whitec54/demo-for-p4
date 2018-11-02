#!/usr/local/bin/python3

import sys

for line in sys.stdin:
    if line.strip() == '':
        continue
    print(int(line.strip()) * 2)