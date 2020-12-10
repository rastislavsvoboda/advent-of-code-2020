from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import functools
import copy
import re
import time

# .\get.ps1 10

start = datetime.now()
lines = open('10.in').readlines()

xs = [int(x) for x in lines]
xs.append(0)
xs = sorted(xs)
xs.append(max(xs) + 3)

n1 = 0
n3 = 0
for i in range(len(xs) - 1):
    d = xs[i + 1] - xs[i]
    if d == 1:
        n1 += 1
    elif d == 3:
        n3 += 1

p1 = n1 * n3

# dynamic programming
DP = {}

# dp(i) = the number of ways to complete the adapter chain given
#         that you are currently at adapter xs[i]


def dp(i):
    if i == len(xs) - 1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i + 1, len(xs)):
        if xs[j] - xs[i] <= 3:
            # one way to get from i to the end is to first step to j
            # the number of paths from i that *start* by stepping to xs[j] is DP[j]
            ans += dp(j)
    # memoize
    DP[i] = ans
    return ans


p2 = dp(0)

print(p1)  # 2310
print(p2)  # 64793042714624

stop = datetime.now()
print("duration:", stop - start)