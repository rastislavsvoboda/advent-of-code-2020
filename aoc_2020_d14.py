from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
from itertools import combinations
import copy
import re
import time

# .\get.ps1 14

start = datetime.now()
lines = open('14.in').readlines()

M={}
# A=set()

def to_bin_str(val, d=36):
    bin_str = str(bin(int(val, 10)))[2:]  # starts with 0b
    # if does always start with 1, so some zeros can be missing
    l = len(bin_str)
    if l < d:
        padding = d-l
        bin_str = (padding * '0') + bin_str
    return bin_str


def write(mask, addr, val):
    # print(mask, mem)
    val_b = to_bin_str(val)
    v = ""
    x = 0
    for i in range(36):
        if mask[i] == "1":
            v += "1"
            x += 2**(35-i)
        elif mask[i] == "0":
            v += "0"
        else:
            v += val_b[i]
            if val_b[i] == "1":
                x += 2**(35-i)

    res_val = int(v,2)
    assert res_val == x
    M[int(addr)] = res_val


def get_cmb(x):
    L = []
    for i in range(2**x):
        L.append(to_bin_str(str(i),x))
    return L


def write2(mask, addr, val):
    # print(mask, mem)
    addr_b = to_bin_str(addr)
    a = ""
    # x = 0
    cnt_x=0
    for i in range(36):
        if mask[i] == "1":
            a += "1"
            # x += 2**(35-i)
        elif mask[i] == "0":
            # v += "0"
            a += addr_b[i]
        else:
            a += mask[i]
            # v += val_b[i]
            # if val_b[i] == "1":
            #     x += 2**(35-i)
            cnt_x +=1

    addrs=[]
    cmbs = get_cmb(cnt_x)
    for c in cmbs:
        ci = 0
        ax = ""
        for ai in a:
            if ai == 'X':
                ax += c[ci]
                ci+=1
            else:
                ax+=ai
        addrs.append(ax)

    val = int(val)

    for aa in addrs:
        M[int(aa,2)] = val    


    # res_val = int(v,2)
    # assert res_val == x


def solve1(lines, p1):
    res = 0
    cnt=0
    cnt_v=0
    mask=""
    for line in lines:
        line = line.strip()
        words = line.split()
        # if line == "":
        #     write(mask, mem)
        #     cnt+=1
        #     cnt_v += len(mem)
        if words[0] == "mask":
            mask = words[2]
            # print(mask)
            # if mem != []:
            #     write(mask, mem)
            #     cnt+=1
            #     cnt_v += len(mem)
            #     mem=[]
        else:
            nums = re.findall("\d+", line)
            assert len(nums) ==2 
            # mem.append((nums[0],nums[1]))
            if p1:
                write(mask, nums[0], nums[1])
            else:
                write2(mask, nums[0], nums[1])
            # A.add(nums[0])
    # print(M)
    
    res = sum(M.values())

    print(cnt, cnt_v)
    # s = 0
    # for k, v in M.items()    :
    #     s += v
    # res = s

    return res




# print(solve1(lines, True))  # 14722016054794
print(solve1(lines, False))  # 3618217244644


stop = datetime.now()
print("duration:", stop - start)