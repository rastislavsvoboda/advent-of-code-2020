from datetime import datetime
from collections import defaultdict

# .\get.ps1 21

start = datetime.now()
lines = open('21.in').readlines()

allergens = set()
possible = dict()
counts = defaultdict(int)
for line in lines:
    left, right = line.strip().split('(contains ')
    Is = left.split() # Ingredients
    As = right[:-1].split(', ') # Allergens
    for a in As:
        allergens.add(a)
        if a not in possible:
            possible[a] = set(Is)
        else:
            possible[a] &= set(Is)
    for i in Is:
        counts[i] += 1

# print("allergens cnt", len(allergens))

ASSIGN = {}

while len(ASSIGN) < len(allergens):
    found_ingrd = None
    for allerg, ingrds in possible.items():
        if len(ingrds) == 1:
            found_ingrd = ingrds.pop()
            ASSIGN[found_ingrd] = allerg
            break
    assert found_ingrd
    for ingrds in possible.values():
        ingrds.discard(found_ingrd)
    del possible[ASSIGN[found_ingrd]]

# print(ASSIGN)
res1 = 0
for ingrd, cnt in counts.items():
    if ingrd not in ASSIGN:
        res1 += cnt

print("part1:", res1)  # 2874

sorted_by_allerg = sorted(ASSIGN.items(), key=lambda pair: pair[1])
res2 = ",".join(map(lambda pair: pair[0], sorted_by_allerg))
print("part2:", res2)  # gfvrr,ndkkq,jxcxh,bthjz,sgzr,mbkbn,pkkg,mjbtz

stop = datetime.now()
print("duration:", stop - start)