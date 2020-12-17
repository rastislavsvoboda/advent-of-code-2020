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
                cube = M.get((x + dx, y + dy, z + dz), '.')
                if cube == "#":
                    cnt += 1
    return cnt


def evolve1(M, sizeX, sizeY, sizeZ):
    newM = copy.deepcopy(M)
    sizeX += 1
    sizeY += 1
    sizeZ += 1
    for z in range(-sizeZ, sizeZ + 1):
        for y in range(-sizeY, sizeY + 1):
            for x in range(-sizeX, sizeX + 1):
                p = (x, y, z)
                cube = M.get(p, '.')
                cnt = adj1(M, p)
                if cube == "#" and cnt not in [2, 3]:
                    newM[p] = "."
                elif cube == '.' and cnt == 3:
                    newM[p] = "#"
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
                    cube = M.get((x + dx, y + dy, z + dz, w + dw), '.')
                    if cube == "#":
                        cnt += 1
    return cnt


def evolve2(M, sizeX, sizeY, sizeZ, sizeW):
    newM = copy.deepcopy(M)
    sizeX += 1
    sizeY += 1
    sizeZ += 1
    sizeW += 1
    for w in range(-sizeW, sizeW + 1):
        for z in range(-sizeZ, sizeZ + 1):
            for y in range(-sizeY, sizeY + 1):
                for x in range(-sizeX, sizeX + 1):
                    p = (x, y, z, w)
                    cube = M.get(p, '.')
                    cnt = adj2(M, p)
                    if cube == "#" and cnt not in [2, 3]:
                        newM[p] = "."
                    elif cube == '.' and cnt == 3:
                        newM[p] = "#"
    return newM, sizeX, sizeY, sizeZ, sizeW


def count(M):
    res = 0
    for v in M.values():
        if v == "#":
            res += 1
    return res


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
    M = {}
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    sizeZ = 0

    for z in range(-sizeZ, sizeZ + 1):
        for y in range(-sizeY, sizeY + 1):
            for x in range(-sizeX, sizeX + 1):
                M[(x, y, z)] = '.'

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            M[(x - sizeX, y - sizeY, 0)] = c
    # printM1(M, sizeX, sizeY, sizeZ)
    # print("----------------")

    cycle = 0
    while cycle < 6:
        M, sizeX, sizeY, sizeZ = evolve1(M, sizeX, sizeY, sizeZ)
        cycle += 1
        # printM1(M, sizeX, sizeY, sizeZ)
        # print("----------------")

    res = count(M)
    return res


def solve2(lines):
    M = {}
    sizeX = len(lines[0]) // 2
    sizeY = len(lines) // 2
    sizeZ = 0
    sizeW = 0

    for w in range(-sizeW, sizeW + 1):
        for z in range(-sizeZ, sizeZ + 1):
            for y in range(-sizeY, sizeY + 1):
                for x in range(-sizeX, sizeX + 1):
                    M[(x, y, z, w)] = '.'

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            M[(x - sizeX, y - sizeY, 0, 0)] = c

    cycle = 0
    while cycle < 6:
        M, sizeX, sizeY, sizeZ, sizeW = evolve2(M, sizeX, sizeY, sizeZ, sizeW)
        cycle += 1

    res = count(M)
    return res


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)