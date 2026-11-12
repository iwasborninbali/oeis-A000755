#!/usr/bin/env python3
"""Collinearity check of Flammenkamp's n = 20 representative configurations (written by the lab's guide, 13 Nov 2026).

Decodes each line by its own rules (first character = symmetry class, then for every row y the two columns as base-89
digits; the alphabet is the one of the database's readme), and checks that no three of the 2n points are collinear:
for every point the reduced directions to all later points are pairwise distinct. Shares no code with check_orbits.py.
Usage: python3 -I check_collinear.py DATA_DIR
"""
import os
import sys
from math import gcd

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,."
FILES = ["n20_iden", "n20_dia1", "n20_dia2", "n20_rot2", "n20_rot4"]


def no_three(pts):
    for i, (x, y) in enumerate(pts):
        seen = set()
        for u, v in pts[i + 1:]:
            dx, dy = u - x, v - y
            g = gcd(abs(dx), abs(dy))
            d = (dx // g, dy // g)
            if d[0] < 0 or (d[0] == 0 and d[1] < 0):
                d = (-d[0], -d[1])
            if d in seen:
                return False
            seen.add(d)
    return True


total = 0
for name in FILES:
    lines = [l.strip() for l in open(os.path.join(sys.argv[1], name)) if l.strip()]
    for line in lines:
        cols = [ALPHABET.index(c) for c in line[1:]]
        n = len(cols) // 2
        assert n == 20 and len(cols) == 40, line
        pts = [(cols[2 * y + j], y) for y in range(n) for j in (0, 1)]
        assert len(set(pts)) == 40 and all(0 <= x < n for x, _ in pts), line
        if not no_three(pts):
            sys.exit(f"FAIL {name}: three collinear points in {line}")
    print(name, len(lines), "configurations, no three collinear in any")
    total += len(lines)
print("total", total, "representatives checked")
