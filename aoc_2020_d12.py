from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time
import math

# .\get.ps1 12

start = datetime.now()
lines = open('12.in').readlines()


def solve1(lines):
    res = 0
    (y, x) = (0, 0)

    DIRS = "NESW"
    hd = 1

    for line in lines:
        line = line.strip()
        dr, val = line[0], int(line[1:])
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
    res = abs(x) + abs(y)
    return res


def heading(wy, wx):
    h = ""
    h += "N" if wy <= 0 else "S"
    h += "E" if wx >= 0 else "W"
    return h


def solve2(lines):
    res = 0
    # position
    (y, x) = (0, 0)
    # waypoint position
    (wy, wx) = (-1, 10)

    DIRS = "NESW"
    hd = 1

    for line in lines:
        line = line.strip()
        dr, val = line[0], int(line[1:])
        head = DIRS[hd]
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
        elif dr == "L":
            wh = heading(wy, wx)
            if val == 90:
                if wh == "NE":
                    wy, wx = -abs(wx), -abs(wy)
                elif wh == "NW":
                    wy, wx = abs(wx), -abs(wy)
                elif wh == "SW":
                    wy, wx = abs(wx), abs(wy)
                elif wh == "SE":
                    wy, wx = -abs(wx), abs(wy)
                else:
                    assert False, wh
            elif val == 180:
                wy, wx = -wy, -wx
            elif val == 270:
                if wh == "NE":
                    wy, wx = abs(wx), abs(wy)
                elif wh == "NW":
                    wy, wx = -abs(wx), abs(wy)
                elif wh == "SW":
                    wy, wx = -abs(wx), -abs(wy)
                elif wh == "SE":
                    wy, wx = abs(wx), -abs(wy)
                else:
                    assert False, wh
        elif dr == "R":
            wh = heading(wy, wx)
            if val == 90:
                if wh == "NE":
                    wy, wx = abs(wx), abs(wy)
                elif wh == "NW":
                    wy, wx = -abs(wx), abs(wy)
                elif wh == "SW":
                    wy, wx = -abs(wx), -abs(wy)
                elif wh == "SE":
                    wy, wx = abs(wx), -abs(wy)
                else:
                    assert False, wh
            elif val == 180:
                wy, wx = -wy, -wx
            elif val == 270:
                if wh == "NE":
                    wy, wx = -abs(wx), -abs(wy)
                elif wh == "NW":
                    wy, wx = abs(wx), -abs(wy)
                elif wh == "SW":
                    wy, wx = abs(wx), abs(wy)
                elif wh == "SE":
                    wy, wx = -abs(wx), abs(wy)
                else:
                    assert False, wh

    res = abs(x) + abs(y)
    return res


print(solve1(lines))  # 636
print(solve2(lines))  # 26841

stop = datetime.now()
print("duration:", stop - start)