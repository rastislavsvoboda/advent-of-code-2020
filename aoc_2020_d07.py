from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 7

start = datetime.now()
lines = open('7.in').readlines()


def get_outside_bags(name, bags):
    all_outside_bags = set()
    for outside_name, inside_bags in iter(bags.items()):
        for _, inside_name in inside_bags:
            if inside_name == name:
                all_outside_bags.add(outside_name)
    return all_outside_bags


def count_bags(name, bags):
    if bags[name] == []:
        # no inside bags, count only itself
        return 1

    x = 1
    for num, inside_name in bags[name]:
        x += num * count_bags(inside_name, bags)

    return x


def get_data(lines):
    bags = {}
    for line in lines:
        words = line.strip().split()
        src = " ".join(words[0:2])
        dst = []
        if words[4:6] == ["no", "other"]:
            bags[src] = dst
        else:
            inside = words[4:]
            for i in range(0, len(inside), 4):
                num = int(inside[i])
                name = " ".join(inside[i + 1:i + 3])
                dst.append((num, name))
            bags[src] = dst
    return bags


def solve1(lines):
    bags = get_data(lines)
    seen = set()
    todo = deque()
    todo.append("shiny gold")
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        seen.add(name)
        for bag in get_outside_bags(name, bags):
            todo.append(bag)
    res = len(seen) - 1
    return res


def solve2(lines):
    bags = get_data(lines)
    res = count_bags("shiny gold", bags) - 1
    return res


print(solve1(lines))  # 142
print(solve2(lines))  # 10219

stop = datetime.now()
print("duration:", stop - start)