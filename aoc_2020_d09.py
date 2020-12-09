from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 9

start = datetime.now()
lines = open('9.in').readlines()


def is_sum(arr, indx, pream):
    sub_arr = arr[indx - pream:indx]
    for i in range(len(sub_arr)):
        for j in range(i, len(sub_arr)):
            if sub_arr[i] + sub_arr[j] == arr[indx]:
                return True
    return False


def find_range(arr, target):
    for i in range(len(arr)):
        s = arr[i]
        for j in range(i + 1, len(arr)):
            s += arr[j]
            if s == target:
                return arr[i:j + 1]
            if s > target:
                break
    return None


def solve(lines):
    res1 = None
    res2 = None
    A = []
    for line in lines:
        line = line.strip()
        A.append(int(line))
    pream = 25
    i = pream
    while i < len(A):
        if not is_sum(A, i, pream):
            res1 = A[i]
            break
        i += 1
    assert res1 is not None
    cont_range = find_range(A, res1)
    assert cont_range is not None
    sorted_range = list(sorted(cont_range))
    res2 = sorted_range[0] + sorted_range[-1]
    return res1, res2


print(solve(lines))  # 144381670, 20532569

stop = datetime.now()
print("duration:", stop - start)