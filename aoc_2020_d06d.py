from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import functools
import copy
import re
import time

# .\get.ps1 6

start = datetime.now()
lines = open('6.in').read()

data = []
groups = lines.split('\n\n')
for grp in groups:
    g = []
    for ans in grp.split():
        g.append(set(ans))
    data.append(g)

print(sum(map(lambda grp: len(functools.reduce(lambda a, b: a.union(b), grp)), data)))
# print(sum(map(lambda grp: len(functools.reduce(lambda a, b: a | b, grp)), data)))
print(sum(map(lambda grp: len(functools.reduce(lambda a, b: a.intersection(b), grp)), data)))
# print(sum(map(lambda grp: len(functools.reduce(lambda a, b: a & b, grp)), data)))



stop = datetime.now()
print("duration:", stop - start)