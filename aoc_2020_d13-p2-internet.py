from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 13

start = datetime.now()
lines = open('13.in').readlines()


def find_bus_cadence(a, b, start, offset):
    n = start
    while (n - offset) % a != 0:
        n += b
    m = n + b
    while (m - offset) % a != 0:
        m += b
    return n, m - n


def solve2(lines):
    _, busses = lines[0], lines[1]
    busses = [int(b) if b != 'x' else None for b in busses.split(',')][::-1]
    offset = 0
    cadence = busses[0]
    answer = busses[0]
    for b in busses[1:]:
        offset += 1
        if b is None:
            continue
        answer, cadence = find_bus_cadence(b, cadence, answer, offset)
    answer -= offset
    return answer


print(solve2(lines))  # 556100168221141

stop = datetime.now()
print("duration:", stop - start)