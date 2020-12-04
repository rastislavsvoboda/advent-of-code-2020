from datetime import datetime
from datetime import timedelta
import time

start = datetime.now()
lines = open('1.in').readlines()


def solve1(data):
    res = 0
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] + data[j] == 2020:
                res = data[i] * data[j]
                break
    return res


def solve2(data):
    res = 0
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if data[i] + data[j] + data[k] == 2020:
                    res = data[i] * data[j] * data[k]
                    break
    return res

data = [int(x) for x in lines]
print(solve1(data))  # 326211
print(solve2(data))  # 131347190

stop = datetime.now()
print("duration:", stop - start)