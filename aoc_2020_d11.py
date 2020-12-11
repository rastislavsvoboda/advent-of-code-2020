from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 11

start = datetime.now()
lines = open('11.in').readlines()


def print_state(state):
    for line in state:
        print(''.join(line))


def count_occ(state):
    cnt = 0
    Y = len(state)
    X = len(state[0])
    for y in range(Y):
        for x in range(X):
            if state[y][x] == "#":
                cnt += 1
    return cnt


def count_adj1(state, y, x):
    cnt = 0
    Y = len(state)
    X = len(state[0])
    DY = [-1, 1, 0, 0, -1, 1, -1, 1]
    DX = [0, 0, -1, 1, -1, -1, 1, 1]
    for d in range(8):
        yy = y + DY[d]
        xx = x + DX[d]
        if 0 <= yy < Y and 0 <= xx < X and state[yy][xx] == '#':
            cnt += 1
    return cnt


def solve1(lines):
    state = [list(line.strip()) for line in lines]
    while True:
        change = False
        new_state = copy.deepcopy(state)
        for y, line in enumerate(state):
            for x, c in enumerate(line):
                if c == '.':
                    continue
                cnt = count_adj1(state, y, x)
                if c == 'L' and cnt == 0:
                    new_state[y][x] = '#'
                    change = True
                elif c == '#' and cnt >= 4:
                    new_state[y][x] = 'L'
                    change = True
        state = new_state
        if not change:
            break
    return count_occ(state)


def count_adj2(state, y, x):
    cnt = 0
    Y = len(state)
    X = len(state[0])
    DY = [-1, 1, 0, 0, -1, 1, -1, 1]
    DX = [0, 0, -1, 1, -1, -1, 1, 1]
    for d in range(8):
        yy = y + DY[d]
        xx = x + DX[d]
        while 0 <= yy < Y and 0 <= xx < X and state[yy][xx] == '.':
            yy += DY[d]
            xx += DX[d]
        if 0 <= yy < Y and 0 <= xx < X and state[yy][xx] == '#':
            cnt += 1
    return cnt


def solve2(lines):
    state = [list(line.strip()) for line in lines]
    while True:
        changed = False
        new_state = copy.deepcopy(state)
        for y, line in enumerate(state):
            for x, c in enumerate(line):
                if c == '.':
                    continue
                cnt = count_adj2(state, y, x)
                if c == 'L' and cnt == 0:
                    new_state[y][x] = '#'
                    changed = True
                elif c == '#' and cnt >= 5:
                    new_state[y][x] = 'L'
                    changed = True
        state = new_state
        if not changed:
            break
    return count_occ(state)


print(solve1(lines))  # 2346
print(solve2(lines))  # 2111

stop = datetime.now()
print("duration:", stop - start)