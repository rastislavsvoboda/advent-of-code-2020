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


def write1(mask, addr, val, mem):
    val_b = format(val, F'036b')
    new_val_b = ""
    for i in range(36):
        if mask[i] == "1":
            new_val_b += "1"
        elif mask[i] == "0":
            new_val_b += "0"
        else:
            new_val_b += val_b[i]
    new_val_d = int(new_val_b, 2)
    mem[int(addr)] = new_val_d


def write2(mask, addr, val, mem):
    addr_b = format(addr, F'036b')
    new_addr_b = ""
    xs = []
    for i in range(36):
        if mask[i] == "1":
            new_addr_b += "1"
        elif mask[i] == "0":
            new_addr_b += addr_b[i]
        else:
            new_addr_b += mask[i]
            xs.append(i)
    for c in range(2**len(xs)):
        subst_bits = list(format(c, F"0{len(xs)}b")) if xs!=[] else []
        addr_bits = list(new_addr_b)
        for indx, bit in zip(xs, subst_bits):
            addr_bits[indx] = bit
        mem[int("".join(addr_bits), 2)] = val


def solve(lines, p1):
    MEM = {}
    mask = ""
    for line in lines:
        line = line.strip()
        words = line.split()
        if words[0] == "mask":
            mask = words[2]
        else:
            nums = re.findall("\d+", line)
            assert len(nums) == 2
            if p1:
                write1(mask, int(nums[0]), int(nums[1]), MEM)
            else:
                write2(mask, int(nums[0]), int(nums[1]), MEM)
    return sum(MEM.values())


print(solve(lines, True))  # 14722016054794
print(solve(lines, False))  # 3618217244644

stop = datetime.now()
print("duration:", stop - start)