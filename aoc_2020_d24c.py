from datetime import datetime
from copy import deepcopy

# .\get.ps1 24

start = datetime.now()
lines = open('24.in').readlines()


def get_tile_pos(line, m):
    x, y, z = 0, 0, 0
    i = 0
    while i < len(line):
        c = line[i:i + 1]
        cc = line[i:i + 2]
        if c in m:
            dx, dy, dz = m[c]
            i += 1
        elif cc in m:
            dx, dy, dz = m[cc]
            i += 2
        else:
            assert False
        x += dx
        y += dy
        z += dz
    return (x, y, z)


def solve(lines):
    M = {
        "e": (1, -1, 0),
        "w": (-1, 1, 0),
        "ne": (1, 0, -1),
        "nw": (0, 1, -1),
        "se": (0, -1, 1),
        "sw": (-1, 0, 1)
    }
    blacks = set()
    for line in lines:
        line = line.strip()
        pos = get_tile_pos(line, M)
        if pos in blacks:
            blacks.remove(pos)
        else:
            blacks.add(pos)
    res1 = len(blacks)
    # part 2
    for day in range(100):
        new_blacks = set()
        to_check = set()
        for (x, y, z) in blacks:
            to_check.add((x, y, z))
            for dx, dy, dz in M.values():
                to_check.add((x + dx, y + dy, z + dz))

        for (x, y, z) in to_check:
            cnt = 0
            for dx, dy, dz in M.values():
                p = (x + dx, y + dy, z + dz)
                if p in blacks:
                    cnt += 1
            is_black = (x, y, z) in blacks
            if is_black and not (cnt == 0 or cnt > 2):
                new_blacks.add((x, y, z))
            elif not is_black and cnt == 2:
                new_blacks.add((x, y, z))

        blacks = new_blacks
        # res = len(blacks)
        # print(F"Day {day+1}: {res}")
    res2 = len(blacks)
    return res1, res2


print(solve(lines))  # 287, 3636

stop = datetime.now()
print("duration:", stop - start)