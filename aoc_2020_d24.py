from datetime import datetime
import copy

# .\get.ps1 24

start = datetime.now()
lines = open('24.in').readlines()


def get_tile_pos(line):
    x, y = 0, 0
    i = 0
    while i < len(line):
        c = line[i:i + 1]
        cc = line[i:i + 2]
        if c == "w":
            x -= 2
            i += 1
        elif c == "e":
            x += 2
            i += 1
        elif cc == "nw":
            x -= 1
            y -= 1
            i += 2
        elif cc == "se":
            x += 1
            y += 1
            i += 2
        elif cc == "ne":
            x += 1
            y -= 1
            i += 2
        elif cc == "sw":
            x -= 1
            y += 1
            i += 2
    return (x, y)


def solve(lines):
    T = {}
    for line in lines:
        line = line.strip()
        pos = get_tile_pos(line)
        tile = T.get(pos, "w")
        if tile == "w":
            T[pos] = "b"
        else:
            T[pos] = "w"
    res1 = sum([1 for x in T.values() if x == "b"])

    ADJS = [(-2, 0), (2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for day in range(100):
        newT = copy.deepcopy(T)
        xs = list(map(lambda k: k[0], T.keys()))
        ys = list(map(lambda k: k[1], T.keys()))
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)

        for x in range(min(xs) - 1, max(xs) + 2):
            for y in range(min(ys) - 1, max(ys) + 2):
                if (x % 2) != (y % 2):
                    continue
                cnt = 0
                for dx, dy in ADJS:
                    p = (x + dx, y + dy)
                    if T.get(p, "w") == "b":
                        cnt += 1
                tile = T.get((x, y), "w")
                if tile == "b" and (cnt == 0 or cnt > 2):
                    newT[(x, y)] = "w"
                elif tile == "w" and cnt == 2:
                    newT[(x, y)] = "b"
        T = newT
        # res = sum([1 for x in T.values() if x == "b"])
        # print(F"Day {day+1}: {res}")

    res2 = sum([1 for x in T.values() if x == "b"])
    return res1, res2


print(solve(lines))  # 287, 3636

stop = datetime.now()
print("duration:", stop - start)