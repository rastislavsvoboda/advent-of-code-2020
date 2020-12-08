from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
from copy import deepcopy
import re
import time

# .\get.ps1 8

start = datetime.now()
lines = open('8.in').readlines()
# lines = open('8.0').readlines()

def process(instr, ip, acc):
    cmd = instr[0]
    val = int(instr[1])
    if cmd == "nop":
        None
    if cmd == "acc":
        acc = acc + val
    if cmd == "jmp":
        ip += val
        return ip, acc
    return (ip + 1, acc)


def solve1(lines):
    data = [line.split() for line in lines]
    seen = set()
    ip = 0
    acc = 0
    while ip < len(data):
        if ip in seen:
            # if instruction repeats, we are done
            break
        seen.add(ip)
        ip, acc = process(data[ip], ip, acc)
    return acc


def solve2(lines):
    original = [line.split() for line in lines]
    for i in range(len(lines)):
        data = deepcopy(original)
        # modify exactly one nop -> jmp or jmp -> nop
        if data[i][0] == "nop":
            data[i][0] = "jmp"
        elif data[i][0] == "jmp":
            data[i][0] = "nop"
        else:
            continue

        acc = 0
        ip = 0
        seen = set()
        done = True
        
        while ip < len(data):
            if ip in seen:
                done = False
                break
            seen.add(ip)
            ip, acc = process(data[ip], ip, acc)

        if done:
            break

    return acc


print(solve1(lines))  # 1548
print(solve2(lines))  # 1375

stop = datetime.now()
print("duration:", stop - start)