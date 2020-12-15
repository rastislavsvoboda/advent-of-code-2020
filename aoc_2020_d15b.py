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
    history = {}
    for n in nums[:-1]:
        turn += 1
        history[n] = turn
    last_num = nums[-1]
    while True:
        turn += 1
        history[last_num] = turn
        prev_turn = history.get(last_num, -1)
        if prev_turn == -1:
            next_num = 0  # first time spoken
        else:
            next_num = turn - prev_turn  # age
        if turn == limit:
            break
        last_num = next_num
    return last_num


print(solve(lines, 2020))  # 273
print(solve(lines, 30000000))  # 47205

stop = datetime.now()
print("duration:", stop - start)