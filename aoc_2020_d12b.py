from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import functools
import copy
import re
import time
import math

# .\get.ps1 12

start = datetime.now()
lines = open('12.in').readlines()


def parse(line):
    return (line[0], int(line[1:]))

def process1(acc, line):
    dr, val = line
    y, x, hd = acc
    DIRS = "NESW"
    head = DIRS[hd]
    if dr == "N":
        y -= val
    elif dr == "S":
        y += val
    elif dr == "E":
        x += val
    elif dr == "W":
        x -= val
    elif dr == "F":
        if head == "N":
            y -= val
        elif head == "S":
            y += val
        elif head == "E":
            x += val
        elif head == "W":
            x -= val
    elif dr == "L":
        st = val // 90
        hd = (hd - st) % 4
    elif dr == "R":
        st = val // 90
        hd = (hd + st) % 4
    return (y, x, hd)


def get_res1(acc):
    y, x, _ = acc
    return abs(y) + abs(x)


def process2(acc, line):
    dr, val = line
    y, x, wy, wx = acc
    if dr == "N":
        wy -= val
    elif dr == "S":
        wy += val
    elif dr == "E":
        wx += val
    elif dr == "W":
        wx -= val
    elif dr == "F":
        y += val * wy
        x += val * wx
    else:
        assert dr in ["L", "R"]
        if val == 180:
            wy, wx = -wy, -wx

        # waypoint heading
        wh = ("N" if wy <= 0 else "S") + ("E" if wx >= 0 else "W")

        if (dr == "L" and val == 90) or (dr == "R" and val == 270):
            if wh == "NE":
                wy, wx = -abs(wx), -abs(wy)
            elif wh == "NW":
                wy, wx = abs(wx), -abs(wy)
            elif wh == "SW":
                wy, wx = abs(wx), abs(wy)
            elif wh == "SE":
                wy, wx = -abs(wx), abs(wy)

        if (dr == "R" and val == 90) or (dr == "L" and val == 270):
            if wh == "NE":
                wy, wx = abs(wx), abs(wy)
            elif wh == "NW":
                wy, wx = -abs(wx), abs(wy)
            elif wh == "SW":
                wy, wx = -abs(wx), -abs(wy)
            elif wh == "SE":
                wy, wx = abs(wx), -abs(wy)
    return (y, x, wy, wx)


def get_res2(acc):
    y, x, _, _ = acc
    return abs(y) + abs(x)


def solve1(lines):
    data = map(parse, lines)
    initial = (0, 0, 1)  # (y,x,heading E)
    final = functools.reduce(process1, data, initial)
    return get_res1(final)


def solve2(lines):
    data = map(parse, lines)
    initial = (0, 0, -1, 10)  # (y,x,wy,wx)
    final = functools.reduce(process2, data, initial)
    return get_res2(final)

    # in some FP language it could look like this
    # lines
    # |> List.map(parse)
    # |> List.reduce(process2, initial)
    # |> get_res2


print(solve1(lines))  # 636
print(solve2(lines))  # 26841

stop = datetime.now()
print("duration:", stop - start)