from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


def get_adjs3D(p):
    (x, y, z) = p
    offsets = [-1, 0, 1]
    adjs = []
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                if dx == dy == dz == 0:
                    continue
                adjs.append((x + dx, y + dy, z + dz))
    return adjs


def get_adjs4D(p):
    (x, y, z, w) = p
    offsets = [-1, 0, 1]
    adjs = []
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                for dw in offsets:
                    if dx == dy == dz == dw == 0:
                        continue
                    adjs.append((x + dx, y + dy, z + dz, w + dw))
    return adjs


def solve1(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0))

    for _ in range(6):
        newM = set()
        to_check = set()

        for p in M:
            to_check.add(p)
            for adj in get_adjs3D(p):
                to_check.add(adj)

        for p in to_check:
            cnt = 0
            for adj in get_adjs3D(p):
                if adj in M:
                    cnt += 1
            is_on = p in M
            if is_on and cnt in [2, 3]:
                newM.add(p)
            elif not is_on and cnt == 3:
                newM.add(p)
        M = newM
    res = len(M)
    return res


def solve2(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    offsets = [-1, 0, 1]

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0, 0))

    for _ in range(6):
        newM = set()
        to_check = set()

        for p in M:
            to_check.add(p)
            for adj in get_adjs4D(p):
                to_check.add(adj)

        for p in to_check:
            cnt = 0
            for adj in get_adjs4D(p):
                if adj in M:
                    cnt += 1
            is_on = p in M
            if is_on and cnt in [2, 3]:
                newM.add(p)
            elif not is_on and cnt == 3:
                newM.add(p)
        M = newM
    res = len(M)
    return res


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)