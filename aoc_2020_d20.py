from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
from itertools import permutations
import copy
import math
import re
import time

# .\get.ps1 20

start = datetime.now()
lines = open('20.in').readlines()


def print_g(g):
    for r in range(len(g)):
        print("".join(g[r]))
    print(len(g) * "-")


def get_combs(name, g):
    cmbs = []
    indx = 0
    for j in range(2):
        for i in range(4):
            rotate_grdR(g)
            cmbs.append((name + "-" + str(indx), copy.deepcopy(g)))
            indx += 1
        flip_grdH(g)
    return cmbs


def rotate_grdR(g):
    LG = len(g)
    old = copy.deepcopy(g)
    for r in range(LG):
        for c in range(LG):
            g[c][LG - 1 - r] = old[r][c]


def flip_grdH(g):
    LG = len(g)
    old = copy.deepcopy(g)
    for r in range(LG):
        for c in range(LG):
            g[LG - 1 - r][c] = old[r][c]


# def flip_grdV(g):
#     old = copy.deepcopy(g)
#     for r in range(10):
#         for c in range(10):
#             g[r][9 - c] = old[r][c]


def parse_grid(lines):
    name = lines[0].strip()[5:-1]
    G = []
    for r, line in enumerate(lines[1:10 + 1]):
        row = []
        for c, ch in enumerate(list(line.strip())):
            row.append(ch)
        G.append(row)
    return name, G


def chck_grid_v(g1, g2):
    for r in range(10):
        if g1[r][9] != g2[r][0]:
            return False
    return True


def chck_grid_h(g1, g2):
    for c in range(10):
        if g1[9][c] != g2[0][c]:
            return False
    return True


GRIDS = {}
COMBS = {}
IDX = []
i = 0
for i in range(0, len(lines), 12):
    grd_lines = lines[i:i + 11]
    name, grid = parse_grid(grd_lines)
    GRIDS[name] = grid
    # print_g(grid)
    COMBS[name] = get_combs(name, grid)
    IDX.append(name)

size = int(math.sqrt(len(IDX)))
# print(size)
res_grd = [[None for _ in range(size)] for _ in range(size)]
seen = set()


def place(n):
    if n == size * size:
        return res_grd

    for name in IDX:
        if name in seen:
            continue

        y, x = divmod(n, size)

        cmbs = COMBS[name]
        for nm, cg in cmbs:

            if y > 0:
                _, up_gr = res_grd[y - 1][x]
                if not chck_grid_h(up_gr, cg):
                    continue
            if x > 0:
                _, left_gr = res_grd[y][x - 1]
                if not chck_grid_v(left_gr, cg):
                    continue

            seen.add(name)
            res_grd[y][x] = (nm, cg)
            res = place(n + 1)
            if res:
                return res
            res_grd[y][x] = None
            seen.discard(name)
    return None


gr = place(0)
# print(gr)
a = gr[0][0][0][:4]
b = gr[0][size - 1][0][:4]
c = gr[size - 1][0][0][:4]
d = gr[size - 1][size - 1][0][:4]
# print(a, b, c, d)
print(int(a) * int(b) * int(c) * int(d))  # 2699020245973

# assert False
tileSize = 10
imageSize = tileSize-2

final = [['?' for _ in range(imageSize*size)] for _ in range(imageSize*size)]
assert(len(final) == len(final[0]))

for y, row in enumerate(gr):
    for x,ng in enumerate(row):
        name, grid = ng
        # print_g(grid)
        for r in range(1,tileSize-1):
            for c in range(1,tileSize-1):
                final[y*imageSize+r-1][x*imageSize+c-1] = grid[r][c]
        # print(grid)


# print_g(final)

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()

monst_grd = []
for r, line in enumerate(monster):
    row = [] 
    for c, ch in enumerate(line):
        row.append(ch)
    monst_grd.append(row)

FINAL_R = len(final)
FINAL_C = len(final[0])

MON_R = len(monst_grd)
MON_C = len(monst_grd[0])

final_cmb = get_combs("final", final)

# print_g(monst_grd)

sizes = [-1 for _ in range(len(final_cmb))]
hasMonsters = [ 0 for _ in range(len(final_cmb)) ]
drawed = [ None for _ in range(len(final_cmb)) ]

for i,fcmb in enumerate(final_cmb):
    name, f = fcmb
    for rr in range(0, FINAL_R-MON_R+1):
        for cc in range(0, FINAL_C-MON_C+1):
            all_match = True
            for r in range(MON_R):
                for c in range(MON_C):
                    if monst_grd[r][c] == "#":
                        if f[rr+r][cc+c] != "#":
                            all_match = False
            if all_match:
                hasMonsters[i] += 1
                for r in range(MON_R):
                    for c in range(MON_C):
                        if monst_grd[r][c] == "#":
                            f[rr+r][cc+c] = "O"
                drawed[i] = f


# print(hasMonsters)
for i,mon_cnt in enumerate(hasMonsters):
    if mon_cnt > 0:
        # print_g(drawed[i])
        cnt = 0
        for r, row in enumerate(drawed[i]):
            for c, ch in enumerate(row):
                if ch == "#":
                    cnt+=1
        print(cnt)



                







stop = datetime.now()
print("duration:", stop - start)