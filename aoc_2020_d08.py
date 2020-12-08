from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 8

start = datetime.now()
lines = open('8.in').readlines()
# lines = open('8.0').readlines()

# regs = {"a": 0}

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

    return ip + 1, acc


def solve1(lines):
    data = [line.split(' ') for line in lines]
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
    data = [line.split(' ') for line in lines]
    modified = set()

    for i, line in enumerate(data):
        # modifie eactly one nop -> jmp or jmp -> nop
        if line[0] == "nop" and i not in modified:
            data[i][0] = "jmp"
            modified.add(i)
        elif line[0] == "jmp" and i not in modified:
            data[i][0] = "nop"
            modified.add(i)
        else:
            continue

        done = True
        acc = 0
        seen = set()
        ip = 0
        while ip < len(data):
            if ip in seen:
                done = False
                break
            seen.add(ip)
            ip, acc = process(data[ip], ip, acc)

        if done:
            break

        # use original data
        data = [line.split(' ') for line in lines]

    return acc


print(solve1(lines))  # 1548
print(solve2(lines))  # 1375

stop = datetime.now()
print("duration:", stop - start)