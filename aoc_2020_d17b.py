from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


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


def evolve1(M, sizeX, sizeY, sizeZ):
    newM = set()
    sizeX += 1
    sizeY += 1
    sizeZ += 1
    for z in range(-sizeZ, sizeZ + 1):
        for y in range(-sizeY, sizeY + 1):
            for x in range(-sizeX, sizeX + 1):
                p = (x, y, z)
                alive = p in M
                cnt = adj1(M, p)
                if alive and cnt in [2, 3]:
                    newM.add(p)
                if not alive and cnt == 3:
                    newM.add(p)
    return newM, sizeX, sizeY, sizeZ


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


def evolve2(M, sizeX, sizeY, sizeZ, sizeW):
    newM = set()
    sizeX += 1
    sizeY += 1
    sizeZ += 1
    sizeW += 1
    for w in range(-sizeW, sizeW + 1):
        for z in range(-sizeZ, sizeZ + 1):
            for y in range(-sizeY, sizeY + 1):
                for x in range(-sizeX, sizeX + 1):
                    p = (x, y, z, w)
                    alive = p in M
                    cnt = adj2(M, p)
                    if alive and cnt in [2, 3]:
                        newM.add(p)
                    if not alive and cnt == 3:
                        newM.add(p)
    return newM, sizeX, sizeY, sizeZ, sizeW


def printM1(M, sizeX, sizeY, sizeZ):
    for z in range(-sizeZ, sizeZ + 1):
        print(F"z={z}")
        for y in range(-sizeY, sizeY + 1):
            l = ""
            for x in range(-sizeX, sizeX + 1):
                cube = M.get((x, y, z), '.')
                l += cube
            print(l)
        print()
    print()


def solve1(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    sizeZ = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0))
    # printM1(M, sizeX, sizeY, sizeZ)
    # print("----------------")

    cycle = 0
    while cycle < 6:
        M, sizeX, sizeY, sizeZ = evolve1(M, sizeX, sizeY, sizeZ)
        cycle += 1
        # printM1(M, sizeX, sizeY, sizeZ)
        # print("----------------")

    return len(M)


def solve2(lines):
    M = set()
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    sizeZ = 0
    sizeW = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x - sizeX, y - sizeY, 0, 0))

    cycle = 0
    while cycle < 6:
        M, sizeX, sizeY, sizeZ, sizeW = evolve2(M, sizeX, sizeY, sizeZ, sizeW)
        cycle += 1

    return len(M)


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)