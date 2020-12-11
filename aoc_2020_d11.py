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
                cnt = 0
                if c == '.':
                    continue
                for (yy, xx) in [(y - 1, x), (y + 1, x), (y, x - 1),
                                 (y, x + 1), (y - 1, x - 1), (y + 1, x - 1),
                                 (y - 1, x + 1), (y + 1, x + 1)]:
                    if 0 <= yy < Y and 0 <= xx < X:
                        if state[yy][xx] == '#':
                            cnt += 1
                # print(y,x,cnt)
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

    for i, c in enumerate(serialized):
        if c == "#":
            res += 1

    return res


def count_adj(state, y, x):
    cnt = 0
    Y = len(state)
    X = len(state[0])

    # for (yy, xx) in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1), (y - 1, x - 1), (y + 1, x - 1),  (y - 1, x + 1), (y + 1, x + 1)]:
    for (dy, dx) in [(-1, 0), (+1, 0), (0, -1), (0, +1), (-1, -1), (+1, -1),
                     (-1, +1), (+1, +1)]:

        yy = y - dy
        xx = x - dx

        while True:

            if 0 <= yy < Y and 0 <= xx < X:
                if state[yy][xx] == '.':
                    yy = yy - dy
                    xx = xx - dx
                    continue

                if state[yy][xx] == '#':
                    cnt += 1
                    break
                if state[yy][xx] == 'L':
                    break
            else:
                break

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
                cnt = 0
                if c == '.':
                    continue
                cnt = count_adj(state, y, x)
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

    for i, c in enumerate(serialized):
        if c == "#":
            res += 1

    return res


print(solve1(lines))  # 2346
print(solve2(lines))  # 2111

stop = datetime.now()
print("duration:", stop - start)