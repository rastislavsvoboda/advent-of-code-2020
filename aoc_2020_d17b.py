from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


def range_for(idx, set_):
    return range(min(p[idx] for p in set_) - 1, max(p[idx] for p in set_) + 2)


def adj1(M, p):
    (x, y, z) = p
    cnt = 0
    offsets = [-1, 0, 1]
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                if dx == dy == dz == 0:
                    continue
                if (x + dx, y + dy, z + dz) in M:
                    cnt += 1
    return cnt


def evolve1(M):
    newM = set()
    for z in range_for(2, M):
        for y in range_for(1, M):
            for x in range_for(0, M):
                p = (x, y, z)
                alive = p in M
                cnt = adj1(M, p)
                if alive and cnt in [2, 3]:
                    newM.add(p)
                elif not alive and cnt == 3:
                    newM.add(p)
    return newM


def adj2(M, p):
    (x, y, z, w) = p
    cnt = 0
    offsets = [-1, 0, 1]
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                for dw in offsets:
                    if dx == dy == dz == dw == 0:
                        continue
                    if (x + dx, y + dy, z + dz, w + dw) in M:
                        cnt += 1
    return cnt


def evolve2(M):
    newM = set()
    for w in range_for(3, M):
        for z in range_for(2, M):
            for y in range_for(1, M):
                for x in range_for(0, M):
                    p = (x, y, z, w)
                    alive = p in M
                    cnt = adj2(M, p)
                    if alive and cnt in [2, 3]:
                        newM.add(p)
                    elif not alive and cnt == 3:
                        newM.add(p)
    return newM


def solve1(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0))

    cycle = 0
    while cycle < 6:
        M = evolve1(M)
        cycle += 1

    return len(M)


def solve2(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0, 0))

    cycle = 0
    while cycle < 6:
        M = evolve2(M)
        cycle += 1

    return len(M)


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)