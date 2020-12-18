from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 18

start = datetime.now()
lines = open('18.in').readlines()


class num(int):
    def __sub__(self, b):
        return num(int(self) * int(b))

    def __add__(self, b):
        return num(int(self) + int(b))

    def __mul__(self, b):
        return num(int(self) + int(b))


def solve(lines, p1):
    res = 0
    for line in lines:
        line = line.strip()
        line = line.replace('*', '-')
        if not p1:
            line = line.replace('+', '*')
        line = re.sub('(\d+)', r'num(\1)', line)
        x = eval(line)
        # print(x)
        res += x
    return res


print(solve(lines, True))  # 98621258158412
print(solve(lines, False))  # 241216538527890

stop = datetime.now()
print("duration:", stop - start)