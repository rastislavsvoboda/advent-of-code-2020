from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import itertools
import re
import time

# .\get.ps1 9

start = datetime.now()
lines = open('9.in').readlines()


def is_sum(arr, indx, pream):
    sub_arr = arr[indx - pream:indx]
    for i in range(len(sub_arr)):
        for j in range(i + 1, len(sub_arr)):
            if sub_arr[i] + sub_arr[j] == arr[indx]:
                return True
    return False


def find_range(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sm = sum(arr[i:j + 1])
            if sm == target:
                return arr[i:j + 1]
            if sm > target:
                break
    return None


def solve(lines):
    res1 = None
    res2 = None
    A = [int(x) for x in lines]
    pream = 25
    for i in range(pream, len(A)):
        if not is_sum(A, i, pream):
            res1 = A[i]
            break
    assert res1 is not None
    cont_range = find_range(A, res1)
    assert cont_range is not None
    res2 = min(cont_range) + max(cont_range)
    return res1, res2


print(solve(lines))  # 144381670, 20532569

stop = datetime.now()
print("duration:", stop - start)