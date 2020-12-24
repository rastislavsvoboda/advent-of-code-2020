from datetime import datetime
from copy import deepcopy

# .\get.ps1 24

start = datetime.now()
lines = open('24.in').readlines()

def get_tile_pos(line, m):
    x, y = 0, 0
    i = 0
    while i < len(line):
        c = line[i:i + 1]
        cc = line[i:i + 2]
        if c in m:
            dx, dy = m[c]
            i += 1
        elif cc in m:
            dx, dy = m[cc]
            i += 2
        else:
            assert False
        x += dx
        y += dy
    return (x, y)


def solve(lines):
    M = {
        "e": (2, 0),
        "w": (-2, 0),
        "ne": (1, -1),
        "nw": (-1, -1),
        "se": (1, 1),
        "sw": (-1, 1)
    }    
    T = {}
    for line in lines:
        line = line.strip()
        pos = get_tile_pos(line, M)
        tile = T.get(pos, "w")
        if tile == "w":
            T[pos] = "b"
        else:
            T[pos] = "w"
    count_black = lambda tiles: sum([1 for x in tiles.values() if x == "b"])
    res1 = count_black(T)
    # part 2
    for day in range(100):
        newT = deepcopy(T)
        xs = list(map(lambda k: k[0], T.keys()))
        ys = list(map(lambda k: k[1], T.keys()))
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        for x in range(min(xs) - 1, max(xs) + 2):
            for y in range(min(ys) - 1, max(ys) + 2):
                if (x % 2) != (y % 2):
                    # skip invalid tile pos, must be both odd or both even
                    continue
                cnt = 0
                for dx, dy in M.values():
                    p = (x + dx, y + dy)
                    if T.get(p, "w") == "b":
                        cnt += 1
                tile = T.get((x, y), "w")
                if tile == "b" and (cnt == 0 or cnt > 2):
                    newT[(x, y)] = "w"
                elif tile == "w" and cnt == 2:
                    newT[(x, y)] = "b"
        T = newT
        # res = count_black(T)
        # print(F"Day {day+1}: {res}")
    res2 = count_black(T)
    return res1, res2


print(solve(lines))  # 287, 3636

stop = datetime.now()
print("duration:", stop - start)