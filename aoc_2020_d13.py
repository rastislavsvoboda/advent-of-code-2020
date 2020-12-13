from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
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


def get_time(d):
    i = 2439024390243 * 41
    while True:
        if is_ok(d, i):
            yield i
        i += d[0]


def is_ok(deps, t):
    for k, v in deps.items():

        if (t + k) % v != 0:
            return False
    return True


def solve2(lines):
    res = 0
    deps = lines[1].strip()
    D = {}
    off = 0
    max_bus_num = -1
    max_bus_num_off = -1
    for dep in deps.split(','):
        if dep != 'x':
            num = int(dep)
            D[off] = num
            if num > max_bus_num:
                max_bus_num = num
                max_bus_num_off = off
        off += 1

    print(max_bus_num, max_bus_num_off)
    st = 100000000000000

    print(is_ok(D, 3417))

    # res= next(get_time(D))
    return res


print(solve1(lines))  # 4315
# print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)