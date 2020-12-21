from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import functools
import copy
import re
import time

# .\get.ps1 21

start = datetime.now()
lines = open('21.in').readlines()

alergens = set()
possible = defaultdict(list)
counts = defaultdict(int)
for line in lines:
    line = line.strip()
    st_br = str.index(line, "(")
    ed_br = -1
    assert line[ed_br] == ")"
    alerg_parts = line[st_br + len("contains ") + 1:ed_br].split(", ")
    ingrd_parts = line[:st_br].split()
    for alerg in alerg_parts:
        alergens.add(alerg)
        possible[alerg].append(set(ingrd_parts))
    for ingrd in ingrd_parts:
        counts[ingrd] += 1

# print("alergens cnt", len(alergens))

ASSIGN = {}

for alerg, ingrds in possible.items():
    possible[alerg] = functools.reduce(lambda a, b: a & b, ingrds)

while len(ASSIGN) < len(alergens):
    found = None
    for alerg, ingrds in possible.items():
        if len(ingrds) == 1:
            ingrd = ingrds.pop()
            ASSIGN[ingrd] = alerg
            found = ingrd
            break
    assert found
    for ingrds in possible.values():
        ingrds.discard(found)
    del possible[ASSIGN[found]]

# print(ASSIGN)
res1 = 0
for ingrd, cnt in counts.items():
    if ingrd not in ASSIGN:
        res1 += cnt

print("part1:", res1)  # 2874

sorted_by_alerg = sorted(ASSIGN.items(), key=lambda pair: pair[1])
# print(sorted_by_alerg)
ingreds = list(map(lambda pair: pair[0], sorted_by_alerg))
# print(ingreds)

res2 = ",".join(ingreds)
print("part2:", res2)  # gfvrr,ndkkq,jxcxh,bthjz,sgzr,mbkbn,pkkg,mjbtz

stop = datetime.now()
print("duration:", stop - start)