from datetime import datetime
from collections import defaultdict

# .\get.ps1 21

start = datetime.now()
lines = open('21.in').readlines()

# part 1
allergens = set()
possible = dict()
counts = defaultdict(int)
for line in lines:
    left, right = line.strip().split('(contains ')
    Is = left.split() # Ingredients
    As = right[:-1].split(', ') # Allergens
    allergens |= set(As)
    for a in As:
        if a not in possible:
            possible[a] = set(Is)
        else:
            possible[a] &= set(Is)
    for i in Is:
        counts[i] += 1

# print("allergens cnt", len(allergens))

ASSIGN = {}

while len(ASSIGN) < len(allergens):
    for a in allergens:
        Is = [i for i in possible[a] if i not in ASSIGN]
        if len(Is) == 1:
            ASSIGN[Is[0]] = a
            break

# print(ASSIGN)
res1 = 0
for ingrd, cnt in counts.items():
    if ingrd not in ASSIGN:
        res1 += cnt

print("part1:", res1)  # 2874

# part 2
sorted_by_allerg = sorted(ASSIGN.items(), key=lambda pair: pair[1])
res2 = ",".join(map(lambda pair: pair[0], sorted_by_allerg))
print("part2:", res2)  # gfvrr,ndkkq,jxcxh,bthjz,sgzr,mbkbn,pkkg,mjbtz

stop = datetime.now()
print("duration:", stop - start)