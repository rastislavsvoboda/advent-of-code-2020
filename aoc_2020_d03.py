from datetime import datetime
from datetime import timedelta
import time

# .\get.ps1 3

start = datetime.now()
lines = open('3.in').readlines()


def solve1(data):
    res = 0
    (dc, dr) = (3, 1)
    (c, r) = (dc, dr)
    while r < len(data):
        if data[r][c % len(data[r])] == "#":
            res += 1
        c += dc
        r += dr
    return res


def solve2(data):
    res = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for (dc, dr) in slopes:
        (c, r) = (dc, dr)
        cnt = 0
        while r < len(data):
            if data[r][c % len(data[r])] == "#":
                cnt += 1
            c += dc
            r += dr
        res *= cnt
    return res


data = []
for line in lines:
    data.append(line.strip())

print(solve1(data))  # 292
print(solve2(data))  # 9354744432

stop = datetime.now()
print("duration:", stop - start)