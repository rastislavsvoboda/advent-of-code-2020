from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 15

start = datetime.now()
lines = open('15.in').readlines()


def solve(lines, limit):
    nums = [int(n) for n in lines[0].strip().split(',')]
    turn = 0
    history = defaultdict(list)
    for n in nums:
        turn += 1
        history[n].append(turn)
    last_num = nums[-1]
    while turn < limit:
        prev_turns = history[last_num]
        next_num = 0
        if len(prev_turns) <= 1:
            # first time spoken
            next_num = 0
        else:
            # age
            next_num = turn - prev_turns[-2]
        turn += 1
        history[next_num].append(turn)
        last_num = next_num
    return last_num


print(solve(lines, 2020))  # 273
print(solve(lines, 30000000))  # 47205

stop = datetime.now()
print("duration:", stop - start)