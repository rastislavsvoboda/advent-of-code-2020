from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 11

start = datetime.now()
lines = open('11.in').readlines()


def print_state(state, time):
    print("time", time)
    for line in state:
        print(''.join(line))


def parse_state(lines):
    state = []
    row = []
    for line in lines:
        line = line.strip()
        row = list(line)
        state.append(row)
    return state


def serialize_state(state):
    result = ''.join(map(lambda line: ''.join(line), state))
    return result


def count1(state, y, x):
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
    res = 0
    t = 0
    state = parse_state(lines)
    Y = len(state)
    X = len(state[0])
    history = set()

    t = 0
    # print_state(state, t)
    history.add(serialize_state(state))
    while True:
        new_state = copy.deepcopy(state)
        for y, line in enumerate(state):
            for x, c in enumerate(line):
                if c == '.':
                    continue
                cnt = count1(state, y, x)
                if c == 'L' and cnt == 0:
                    new_state[y][x] = '#'
                elif c == '#' and cnt >= 4:
                    new_state[y][x] = 'L'
        state = new_state
        serialized = serialize_state(state)
        if serialized in history:
            break
        history.add(serialized)
        t += 1
        # print_state(state, t)

    res = sum(c == "#" for c in serialized)
    return res


def count2(state, y, x):
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
    res = 0
    t = 0
    state = parse_state(lines)
    Y = len(state)
    X = len(state[0])
    history = set()

    t = 0
    # print_state(state, t)
    history.add(serialize_state(state))
    while True:
        new_state = copy.deepcopy(state)
        for y, line in enumerate(state):
            for x, c in enumerate(line):
                if c == '.':
                    continue
                cnt = count2(state, y, x)
                if c == 'L' and cnt == 0:
                    new_state[y][x] = '#'
                elif c == '#' and cnt >= 5:
                    new_state[y][x] = 'L'
        state = new_state
        serialized = serialize_state(state)
        if serialized in history:
            break
        history.add(serialized)
        t += 1
        # print_state(state, t)

    res = sum(c == "#" for c in serialized)
    return res


print(solve1(lines))  # 2346
print(solve2(lines))  # 2111

stop = datetime.now()
print("duration:", stop - start)