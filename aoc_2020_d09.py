from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 9

start = datetime.now()
lines = open('9.in').readlines()

def is_sum(A, indx, pream):
    s = indx - pream
    B = A[indx-pream: indx-pream+pream]
    for i in range(len(B)):
        for j in range(i, len(B)):
            if B[i]+B[j]==A[indx]:
                return True
    return False

def is_sum2(A, target):
    for i in range(len(A)):
        s=A[i]
        for j in range(i+1,len(A)):
            s+=A[j]
            if s==target:
                return A[i:j+1]
            if s>target:
                break
    return None



def solve1(lines):
    res = 0

    A=[]
    for line in lines:
        line = line.strip()
        A.append(int(line))
        # print(line)

    pream = 25
    i = pream
    while i<len(A):
        if not is_sum(A,i,pream):
            res = A[i]
            break
        i+=1

    return res

def solve2(lines):
    res = 0

    A=[]
    for line in lines:
        line = line.strip()
        A.append(int(line))
        # print(line)

    pream = 25
    i = pream
    while i<len(A):
        if not is_sum(A,i,pream):
            target = A[i]
            break
        i+=1


    x = is_sum2(A,target)
    x = list(sorted(x))
    a=x[0]
    b=x[-1]
    print(a,b)
    res = a+b    

    return res


print(solve1(lines))  # 144381670
print(solve2(lines))  #
# 13 zle
stop = datetime.now()
print("duration:", stop - start)