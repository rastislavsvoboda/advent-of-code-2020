from datetime import datetime
from datetime import timedelta
import time

start = datetime.now()
lines = open('1.in').readlines()


def solve1(data):
    s = set()
    for a in data:
        s.add(a)
        b = 2020 - a
        if b in s:
            return a * b
    return None


def solve2(data):
    res = None
    n = len(data)
    for i in range(n-1):
        s = set()
        curr_sum = 2020 - data[i]
        for j in range(i + 1, n):
            if (curr_sum-data[j]) in s:
                return data[i] * data[j] * (curr_sum-data[j])
            s.add(data[j])
    return None


data = [int(x) for x in lines]
print(solve1(data))  # 326211
print(solve2(data))  # 131347190

stop = datetime.now()
print("duration:", stop - start)