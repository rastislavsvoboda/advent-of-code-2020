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
    pointers = [None] * (l+1)
    
    s = ns[0]
    for x in ns[1:]:
        pointers[s] = x
        s = x
    pointers[s] = ns[0]

    s_v = ns[0]
    
    for r in range(100):    
        s_next = pointers[s_v]
        p1 = s_next
        p1_next = pointers[p1]
        p2 = p1_next
        p2_next = pointers[p2]
        p3 = p2_next
        p3_next = pointers[p3]

        dst = s_v
        while dst == s_v or dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1 if dst > 1 else l

        dst_next = pointers[dst]
        pointers[s_v] = p3_next
        pointers[dst] = p1
        pointers[p3] = dst_next

        s_v = p3_next

    res = ""
    x = pointers[1]
    while x != 1:
        res += str(x)
        x = pointers[x]

    return res


def solve2(line):
    ns = list(map(int, list(line.strip())))

    highest = max(ns)
    for i in range(highest + 1, 1_000_000 + 1):
        ns.append(i)

    l = len(ns)
    pointers = [None] * (l+1)

    s = ns[0]
    for x in ns[1:]:
        pointers[s] = x
        s = x
    pointers[s] = ns[0]

    s_v = ns[0]
    
    for r in range(10_000_000):    
        s_next = pointers[s_v]
        p1 = s_next
        p1_next = pointers[p1]
        p2 = p1_next
        p2_next = pointers[p2]
        p3 = p2_next
        p3_next = pointers[p3]

        dst = s_v
        while dst == s_v or dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1 if dst > 1 else l

        dst_next = pointers[dst]
        pointers[s_v] = p3_next
        pointers[dst] = p1
        pointers[p3] = dst_next

        s_v = p3_next


    a = pointers[1]
    b = pointers[a]
    res = a * b
    return res


print(solve1(line))  # 26354798
print(solve2(line))  # 166298218695

stop = datetime.now()
print("duration:", stop - start)