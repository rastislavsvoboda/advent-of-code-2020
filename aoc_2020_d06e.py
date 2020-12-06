from datetime import datetime
from datetime import timedelta
import functools
import re
import time

# .\get.ps1 4

start = datetime.now()
lines = open('6.in').read()


def get_data(lines):
    data = []
    for grp in lines.split('\n\n'):
        entries = []
        for row in grp.split():
            entries.append(row)
        data.append(parse_entry(entries))
    return data


def parse_entry(entries):
    answers = []
    for entry in entries:
        answers.append(set(entry))
    return answers


def solve1(lines):
    return sum(map(lambda grp: len(functools.reduce(lambda a, b: a.union(b), grp)), get_data(lines)))
    # return sum(len(functools.reduce(lambda a, b: a.union(b), grp)) for grp in get_data(lines))


def solve2(lines):
    return sum(map(lambda grp: len(functools.reduce(lambda a, b: a.intersection(b), grp)), get_data(lines)))


print(solve1(lines))  # 6930
print(solve2(lines))  # 3585

stop = datetime.now()
print("duration:", stop - start)