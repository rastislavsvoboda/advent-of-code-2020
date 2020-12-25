from datetime import datetime
from itertools import product

# .\get.ps1 17

start = datetime.now()
lines = open('17.in').readlines()


def get_adjs3D(p):
    (x, y, z) = p
    perms = product([-1, 0, 1], repeat=3)
    adjs = [(x + dx, y + dy, z + dz) for dx, dy, dz in perms
            if not (dx == 0 and dy == 0 and dz == 0)]
    return adjs


def get_adjs4D(p):
    (x, y, z, w) = p
    perms = product([-1, 0, 1], repeat=4)
    adjs = [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in perms
            if not (dx == 0 and dy == 0 and dz == 0 and dw == 0)]
    return adjs


def solve1(lines):
    M = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x, y, 0))

    for _ in range(6):
        newM = set()
        to_check = set()

        for p in M:
            to_check.add(p)
            for adj in get_adjs3D(p):
                to_check.add(adj)

        for p in to_check:
            cnt = len([_ for adj in get_adjs3D(p) if adj in M])
            is_on = p in M
            if is_on and (cnt == 2 or cnt == 3):
                newM.add(p)
            elif not is_on and cnt == 3:
                newM.add(p)
        M = newM
    res = len(M)
    return res


def solve2(lines):
    M = set()
    offsets = [-1, 0, 1]

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line.strip())):
            if c == "#":
                M.add((x, y, 0, 0))

    for _ in range(6):
        newM = set()
        to_check = set()

        for p in M:
            to_check.add(p)
            for adj in get_adjs4D(p):
                to_check.add(adj)

        for p in to_check:
            cnt = len([_ for adj in get_adjs4D(p) if adj in M])
            is_on = p in M
            if is_on and (cnt == 2 or cnt == 3):
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