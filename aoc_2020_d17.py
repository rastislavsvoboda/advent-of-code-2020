from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


def adj1(M, x, y, z):
    cnt = 0
    offsets = [-1, 0, 1]
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                if dx == dy == dz == 0:
                    continue
                p = (x + dx, y + dy, z + dz)
                if p in M and M[p] == "#":
                    cnt += 1
    return cnt


def evolve1(M, size):
    newM = copy.deepcopy(M)
    size += 1
    for z in range(-size, size + 1):
        for y in range(-size, size + 1):
            for x in range(-size, size + 1):
                if (x, y, z) not in M:
                    cube = '.'
                else:
                    cube = M[(x, y, z)]
                cnt = adj1(M, x, y, z)
                if cube == "#" and cnt not in [2, 3]:
                    newM[(x, y, z)] = "."
                elif cube == '.' and cnt == 3:
                    newM[(x, y, z)] = "#"
    return newM, size


def adj2(M, x, y, z, w):
    cnt = 0
    offsets = [-1, 0, 1]
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                for dw in offsets:
                    if dx == dy == dz == dw == 0:
                        continue
                    p = (x + dx, y + dy, z + dz, w + dw)
                    if p in M and M[p] == "#":
                        cnt += 1
    return cnt


def evolve2(M, size):
    newM = copy.deepcopy(M)
    size += 1
    for w in range(-size, size + 1):
        for z in range(-size, size + 1):
            for y in range(-size, size + 1):
                for x in range(-size, size + 1):
                    if (x, y, z, w) not in M:
                        cube = '.'
                    else:
                        cube = M[(x, y, z, w)]
                    cnt = adj2(M, x, y, z, w)
                    if cube == "#" and cnt not in [2, 3]:
                        newM[(x, y, z, w)] = "."
                    elif cube == '.' and cnt == 3:
                        newM[(x, y, z, w)] = "#"
    return newM, size


def count(M):
    res = 0
    for v in M.values():
        if v == "#":
            res += 1
    return res


def printM1(M, size):
    for z in range(-size, size + 1):
        print(F"z={z}")
        for y in range(-size, size + 1):
            l = ""
            for x in range(-size, size + 1):
                if (x, y, z) in M:
                    cube = M[(x, y, z)]
                else:
                    cube = '.'
                l += cube
            print(l)
        print()
    print()


def solve1(lines):
    M = {}
    l = len(lines) // 2
    size = l

    for z in range(-size, size + 1):
        for y in range(-size, size + 1):
            for x in range(-size, size + 1):
                M[(x, y, z)] = '.'

    z = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            M[(x - size, y - size, z)] = c
    # printM1(M, size)
    # print("----------------")

    cycle = 0
    while cycle < 6:
        M, size = evolve1(M, size)
        cycle += 1
        # printM1(M, size)
        # print("----------------")

    res = count(M)
    return res


def solve2(lines):
    M = {}
    l = len(lines) // 2
    size = l

    for w in range(-size, size + 1):
        for z in range(-size, size + 1):
            for y in range(-size, size + 1):
                for x in range(-size, size + 1):
                    M[(x, y, z, w)] = '.'

    w = 0
    z = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            M[(x - size, y - size, z, w)] = c

    cycle = 0
    while cycle < 6:
        M, size = evolve2(M, size)
        cycle += 1

    res = count(M)
    return res


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)