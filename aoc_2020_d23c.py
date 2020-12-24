from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 23

start = datetime.now()
lines = open('23.in').readlines()
line = lines[0]


def solve1(line):
    ns = list(map(int, list(line.strip())))
    l = len(ns)
    nums = [None] * (l+1)
    
    s = ns[0]
    for x in ns[1:]:
        nums[s] = x
        s = x
    nums[s] = ns[0]

    s_v = ns[0]
    
    for r in range(100):    
        s_next = nums[s_v]
        p1 = s_next
        p1_next = nums[p1]
        p2 = p1_next
        p2_next = nums[p2]
        p3 = p2_next
        p3_next = nums[p3]

        dst = s_v
        while dst == s_v or dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1 if dst > 1 else l

        dst_next = nums[dst]
        nums[s_v] = p3_next
        nums[dst] = p1
        nums[p3] = dst_next

        s_v = p3_next

    res = ""
    x = nums[1]
    while x != 1:
        res += str(x)
        x = nums[x]

    return res


def solve2(line):
    ns = list(map(int, list(line.strip())))

    highest = max(ns)
    for i in range(highest + 1, 1_000_000 + 1):
        ns.append(i)

    l = len(ns)
    nums = [None] * (l+1)

    s = ns[0]
    for x in ns[1:]:
        nums[s] = x
        s = x
    nums[s] = ns[0]

    s_v = ns[0]
    
    for r in range(10_000_000):    
        s_next = nums[s_v]
        p1 = s_next
        p1_next = nums[p1]
        p2 = p1_next
        p2_next = nums[p2]
        p3 = p2_next
        p3_next = nums[p3]

        dst = s_v
        while dst == s_v or dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1 if dst > 1 else l

        dst_next = nums[dst]
        nums[s_v] = p3_next
        nums[dst] = p1
        nums[p3] = dst_next

        s_v = p3_next


    a = nums[1]
    b = nums[a]
    res = a * b
    return res


print(solve1(line))  # 26354798
print(solve2(line))  # 166298218695

stop = datetime.now()
print("duration:", stop - start)