from datetime import datetime
from datetime import timedelta
import time

# .\get.ps1 12

start = datetime.now()
lines = open('12.in').readlines()


def solve1(lines):
    # 0=N, 1=E, 2=S, 3=W
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]
    x = 0
    y = 0
    dir_ = 1
    for line in lines:
        line = line.strip()
        cmd, n = line[0], int(line[1:])
        if cmd == "N":
            y += n
        elif cmd == "S":
            y -= n
        elif cmd == "E":
            x += n
        elif cmd == "W":
            x -= n
        elif cmd == "L":
            for _ in range(n // 90):
                dir_ = (dir_ + 3) % 4
        elif cmd == "R":
            for _ in range(n // 90):
                dir_ = (dir_ + 1) % 4
        elif cmd == "F":
            x += DX[dir_] * n
            y += DY[dir_] * n
        else:
            assert False, F"unknown command {cmd}"
    return abs(x) + abs(y)


def solve2(lines):
    (y, x) = (0, 0)
    (wy, wx) = (1, 10)
    for line in lines:
        line = line.strip()
        cmd, n = line[0], int(line[1:])
        if cmd == "N":
            wy += n
        elif cmd == "S":
            wy -= n
        elif cmd == "E":
            wx += n
        elif cmd == "W":
            wx -= n
        # https://calcworkshop.com/transformations/rotation-rules/
        # i^2=-1. Multiplying by i is the same as rotating 90 deg
        # (x,y)*i = (x+iy)*i = ix+i^2y = -y+ix = (-y,x)
        # (x,y)*i^3 = (x+iy)*i^3 = i^3x+i^4y = y - ix = (y,-x)
        elif cmd == "L":
            for _ in range(n // 90):
                wx, wy = -wy, wx
        elif cmd == "R":
            for _ in range(n // 90):
                wx, wy = wy, -wx
        elif cmd == "F":
            y += n * wy
            x += n * wx
        else:
            assert False, F"unknown command {cmd}"

    return abs(x) + abs(y)


print(solve1(lines))  # 636
print(solve2(lines))  # 26841

stop = datetime.now()
print("duration:", stop - start)