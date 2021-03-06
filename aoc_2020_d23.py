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
    nums = []
    for x in list(line.strip()):
        nums.append(int(x))

    n = len(nums)
    Q = deque(nums)
    r = 0
    while r < 100:
        r += 1
        sel = Q.popleft()
        p1 = Q.popleft()
        p2 = Q.popleft()
        p3 = Q.popleft()

        dst = sel - 1
        if dst == 0:
            dst = n
        while dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1
            if dst == 0:
                dst = n
        # print(sel, p1, p2, p3, dst)

        # for p2 this is very sloooow
        indx = Q.index(dst)
        Q.insert(indx + 1, p3)
        Q.insert(indx + 1, p2)
        Q.insert(indx + 1, p1)
        Q.append(sel)

    nums = list(Q)
    pos1 = nums.index(1)
    final = nums[pos1 + 1:] + nums[:pos1]
    res = "".join(map(str, final))
    return res


def read(q, m):
    x = q.popleft()
    if x in m:
        a, b, c = m[x]
        # put picked values back to queue in correct order
        # so they appear like they followed x
        q.appendleft(c)
        q.appendleft(b)
        q.appendleft(a)
        del m[x]
    return x


def solve2(line):
    nums = []
    for x in list(line.strip()):
        nums.append(int(x))

    highest = max(nums)
    for i in range(highest + 1, 1_000_000 + 1):
        nums.append(i)

    l = len(nums)
    Q = deque(nums)
    M = {}
    for r in range(10_000_000):
        sel = read(Q, M)
        Q.append(sel)
        
        p1 = read(Q, M)
        p2 = read(Q, M)
        p3 = read(Q, M)
        dst = sel
        while dst == sel or dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1 if dst > 1 else l
        M[dst] = (p1, p2, p3)

        # # this maybe look nicer, but it's ~0.5s slower
        # picked = (read(Q, M), read(Q, M), read(Q, M))
        # dst = sel
        # while dst == sel or dst in picked:
        #     dst = dst - 1 if dst > 1 else l
        # # remember after dst we need to process picked values
        # M[dst] = picked

    # put all memoried values back to Q
    while len(M) > 0:
        x = read(Q, M)
        Q.append(x)

    nums = list(Q)
    assert len(nums) == l
    pos1 = nums.index(1)
    a = nums[(pos1 + 1) % l]
    b = nums[(pos1 + 2) % l]
    res = a * b
    return res


print(solve1(line))  # 26354798
print(solve2(line))  # 166298218695

stop = datetime.now()
print("duration:", stop - start)