from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 15

start = datetime.now()
lines = open('15.in').readlines()


def get_index(nums, num):
    res = []
    for i, n in enumerate(nums):
        if n == num:
            res.append(i)
    return res


def solve1(lines):
    SPOKEN = []
    line = lines[0].strip()
    nums = re.findall(r"\d+", line)
    turn = 0
    prev = 0
    last = 0

    dct = defaultdict(list)



    INDXS = {}

    for i, n in enumerate(nums):
        n = int(n)
        turn += 1
        # SPOKEN.append(int(n))
        INDXS[n] = [turn]
        last = n

    while turn < 2020:
        # last = SPOKEN[-1]

        if last in INDXS:
            indx = INDXS[last]
        else:
            indx = []

        if len(indx) < 2:
            #not in
            prev = 0
        else:
            prev = turn - (indx[-2])

        # SPOKEN.append(prev)
        turn += 1
        if prev in INDXS:
            # INDXS[prev].append(turn)
            INDXS[prev] = INDXS[prev][-1:] + [turn]

        else:
            INDXS[prev]=[turn]

        last=prev
        if (turn % 100000) == 0:
            print(turn)

    # print(SPOKEN)
    # res = SPOKEN[-1]

    return last


def solve2(lines):
    SPOKEN = []
    line = lines[0].strip()
    nums = re.findall(r"\d+", line)
    turn = 0
    prev = 0
    last = 0

    dct = defaultdict(list)



    INDXS = {}

    for i, n in enumerate(nums):
        n = int(n)
        turn += 1
        # SPOKEN.append(int(n))
        INDXS[n] = [turn]
        last = n

    while turn < 30000000:
        # last = SPOKEN[-1]

        if last in INDXS:
            indx = INDXS[last]
        else:
            indx = []

        if len(indx) < 2:
            #not in
            prev = 0
        else:
            prev = turn - (indx[-2])

        # SPOKEN.append(prev)
        turn += 1
        if prev in INDXS:
            # INDXS[prev].append(turn)
            INDXS[prev] = INDXS[prev][-1:] + [turn]

        else:
            INDXS[prev]=[turn]

        last=prev
        # if (turn % 10000000) == 0:
        #     print(turn)
    return last


print(solve1(lines))  # 273
print(solve2(lines))  # 47205

stop = datetime.now()
print("duration:", stop - start)