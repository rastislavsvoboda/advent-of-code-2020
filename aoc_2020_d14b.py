from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 14

start = datetime.now()
lines = open('14.in').readlines()

M={}
# A=set()

def to_bin_str(val):
    bin_str = str(bin(int(val, 10)))[2:]  # starts with 0b
    # if does always start with 1, so some zeros can be missing
    l = len(bin_str)
    if l < 36:
        padding = 36-l
        bin_str = (padding * '0') + bin_str
    return bin_str

def write(mask, mem):
    # print(mask, mem)
    for m in mem:
        addr,val = m
        val_b = to_bin_str(val)
        v = ""
        for i in range(36):
            if mask[i] == "1":
                v += "1"
            elif mask[i] == "0":
                v += "0"
            else:
                v += val_b[i]

        res_val = int(v,2)
        M[int(addr)] = res_val
        # print(mask, addr, val, res_val)


def solve1(lines):
    res = 0
    mem=[]
    mask=""
    lines.append('')
    for line in lines:
        line = line.strip()
        words = line.split()
        if line == "":
            write(mask, mem)
        elif words[0] == "mask":
            if mem != []:
                write(mask, mem)
                mem=[]
            mask = words[2]
        else:
            nums = re.findall("\d+", line)
            assert len(nums) ==2 
            mem.append((nums[0],nums[1]))

    res = sum(M.values())
    return res


print(solve1(lines))  #

stop = datetime.now()
print("duration:", stop - start)