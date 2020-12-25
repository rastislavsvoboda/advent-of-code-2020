from datetime import datetime
from itertools import product

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


def get_adjs3D(p):
    (x, y, z) = p
    offsets = product([-1, 0, 1], repeat=3)
    adjs = [(x + dx, y + dy, z + dz) for dx, dy, dz in offsets
            if (dx, dy, dz) != (0, 0, 0)]
    return adjs


def get_adjs4D(p):
    (x, y, z, w) = p
    offsets = product([-1, 0, 1], repeat=4)
    adjs = [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in offsets
            if (dx, dy, dz, dw) != (0, 0, 0, 0)]
    return adjs


def solve1(lines):
    # will contain only cells that are "on" (#)
    S = set()
    z = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                S.add((x, y, z))

    for _ in range(6):
        newS = set()
        to_check = set()

        for p in S:
            to_check.add(p)
            for adj in get_adjs3D(p):
                to_check.add(adj)

        for p in to_check:
            cnt = len([_ for adj in get_adjs3D(p) if adj in S])
            is_on = p in S
            if (is_on and (cnt == 2 or cnt == 3)) or (not is_on and cnt == 3):
                newS.add(p)
        S = newS
    res = len(S)
    return res


def solve2(lines):
    # will contain only cells that are "on" (#)
    S = set()
    z = w = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                S.add((x, y, z, w))

    for _ in range(6):
        newS = set()
        to_check = set()

        for p in S:
            to_check.add(p)
            for adj in get_adjs4D(p):
                to_check.add(adj)

        for p in to_check:
            cnt = len([_ for adj in get_adjs4D(p) if adj in S])
            is_on = p in S
            if (is_on and (cnt == 2 or cnt == 3)) or (not is_on and cnt == 3):
                newS.add(p)
        S = newS
    res = len(S)
    return res


print(solve1(lines))  # 362
print(solve2(lines))  # 1980

stop = datetime.now()
print("duration:", stop - start)