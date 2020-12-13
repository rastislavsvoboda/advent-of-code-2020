from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque

import itertools
import functools
import copy
import re
import time

# .\get.ps1 13

start = datetime.now()
lines = open('13.in').readlines()


def solve1(lines):
    time = int(lines[0].strip())
    deps = lines[1].strip()
    D = set()
    for dep in deps.split(','):
        if dep == 'x':
            continue
        num = int(dep)
        D.add(num)

    t = time
    busId = 0
    done = False
    while not done:
        for d in D:
            if t % d == 0:
                arr = t
                busId = d
                done = True
                break
        t += 1

    wait = arr - time
    res = wait * busId
    return res


def is_ok(times, char):
    k,v= char
    return filter(lambda t: (t+k) % v == 0, times)


def solve2(lines):
    res = 0
    deps = lines[1].strip()
    D = {}
    off = 0
    for dep in deps.split(','):
        if dep != 'x':
            num = int(dep)
            D[off] = num
        off += 1


    st = 100000000000000
    # st = 556100168221141 - 100
    chars  = map(lambda d: (d, D[d]), D.keys())
    times = functools.reduce(is_ok, chars, itertools.count(st))
    return next(times)


    # res= next(get_time(D))
    # return res


# print(solve1(lines))  # 4315
print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)