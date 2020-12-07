from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 7

start = datetime.now()
lines = open('7.in').readlines()


def count(name, bags):
    total = set()
    for k,val in iter(bags.items()):
        for n,nam in val:
            if nam == name:
                total.add(k)
    return total

def count2(name, bags):
    if bags[name] == []:
        return 1

    x = 1
    for num, nam in bags[name]:
        x += num * count2(nam, bags)

    return x
            


def solve1(lines):
    res = 0
    bags = {}
    for line in lines:
        line = line.strip()
        words = line.split()
        src = " ".join(words[0:2])
        # print(src)
        dst = []
        if words[4:6] == ["no", "other"]:
            bags[src] = dst
        else:
            inside = words[4:]
            # print(inside)
            for i in range(0,len(inside),4):
                n = int(inside[i])
                name = " ".join(inside[i+1:i+3])
                dst.append((n, name))
            bags[src] = dst

        # print(words)
        res += 1
    # print(bags)

    seen = set()
    
    todo = deque()

    todo.append("shiny gold")
    total = set()


    while len(todo) > 0:
        n = todo.pop()

        found = count(n, bags)
        for f in found:
            if f in seen:
                continue
            seen.add(f)
            todo.append(f)
    
    res = len(seen)

    return res

def solve2(lines):
    res = 0
    bags = {}
    for line in lines:
        line = line.strip()
        words = line.split()
        src = " ".join(words[0:2])
        # print(src)
        dst = []
        if words[4:6] == ["no", "other"]:
            bags[src] = dst
        else:
            inside = words[4:]
            # print(inside)
            for i in range(0,len(inside),4):
                n = int(inside[i])
                name = " ".join(inside[i+1:i+3])
                dst.append((n, name))
            bags[src] = dst

        # print(words)
        res += 1
    # print(bags)

    
    res = count2("shiny gold", bags)

    return res - 1



print(solve1(lines))  # 142
print(solve2(lines))  # 10219

stop = datetime.now()
print("duration:", stop - start)