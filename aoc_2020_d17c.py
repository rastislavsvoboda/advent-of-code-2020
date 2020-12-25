from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


def solve1(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    offsets = [-1, 0, 1]

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0))

    for _ in range(6):
        newM = set()
        to_check = set()

        for (x, y, z) in M:
            to_check.add((x, y, z))
            for dx in offsets:
                for dy in offsets:
                    for dz in offsets:
                        if dx == dy == dz == 0:
                            continue
                        to_check.add((x + dx, y + dy, z + dz))

        for (x, y, z) in to_check:
            cnt = 0
            for dx in offsets:
                for dy in offsets:
                    for dz in offsets:
                        if dx == dy == dz == 0:
                            continue
                        if (x + dx, y + dy, z + dz) in M:
                            cnt += 1
            is_on = (x, y, z) in M
            if is_on and cnt in [2, 3]:
                newM.add((x, y, z))
            elif not is_on and cnt == 3:
                newM.add((x, y, z))
        M = newM
    res = len(M)
    return res


def solve2(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    sizeZ = 0
    offsets = [-1, 0, 1]

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0, 0))

    for _ in range(6):
        newM = set()
        to_check = set()

        for (x, y, z, w) in M:
            to_check.add((x, y, z, w))
            for dx in offsets:
                for dy in offsets:
                    for dz in offsets:
                        for dw in offsets:
                            if dx == dy == dz == dw == 0:
                                continue
                            to_check.add((x + dx, y + dy, z + dz, w + dw))

        for (x, y, z, w) in to_check:
            cnt = 0
            for dx in offsets:
                for dy in offsets:
                    for dz in offsets:
                        for dw in offsets:
                            if dx == dy == dz == dw == 0:
                                continue
                            if (x + dx, y + dy, z + dz, w + dw) in M:
                                cnt += 1
            is_on = (x, y, z, w) in M
            if is_on and cnt in [2, 3]:
                newM.add((x, y, z, w))
            elif not is_on and cnt == 3:
                newM.add((x, y, z, w))
        M = newM
    res = len(M)
    return res


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)