from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import functools
import copy
import re
import time

# .\get.ps1 6

start = datetime.now()
lines = open('6.in').read()


def get_data(lines):
    data = []
    groups = lines.split('\n\n')
    for grp in groups:
        g = []
        for ans in grp.split():
            g.append(set(ans))
        data.append(g)
    return data


def solve1(lines):
    res = 0
    data = get_data(lines)
    for grp in data:
        any_qst = functools.reduce(lambda a, b: a.union(b), grp)
        res += len(any_qst)
    return res


def solve2(lines):
    res = 0
    data = get_data(lines)
    for grp in data:
        all_qst = functools.reduce(lambda a, b: a.intersection(b), grp)
        res += len(all_qst)
    return res


print(solve1(lines))  # 6930
print(solve2(lines))  # 3585

stop = datetime.now()
print("duration:", stop - start)