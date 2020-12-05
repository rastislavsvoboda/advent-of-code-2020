from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 0

start = datetime.now()
lines = open('0.in').readlines()


def solve1(lines):
    res = 0
    for line in lines:
        line = line.strip()
        print(line)
        res += 1
    return res


def solve2(lines):
    res = 0
    return res


print(solve1(lines))  #
# print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)