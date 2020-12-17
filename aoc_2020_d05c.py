from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 5

start = datetime.now()
lines = open('5.in').readlines()

p1 = 0
seat_ids = []
for line in lines:
    bin_str = ""
    for ch in line.strip():
        if ch in ['B', 'R']:
            bin_str += '1'
        elif ch in ['F', 'L']:
            bin_str += '0'
        else:
            assert False, F"wrong character {ch}"
    # it's just binary: rrrrrrrccc
    # rrrrrr * 2**3 + ccc 
    seat_id = int(bin_str, 2)
    seat_ids.append(seat_id)
    p1 = max(p1, seat_id)
p2 = None
for id_ in range(p1, 0, -1):
    if (id_ - 1) not in seat_ids:
        p2 = id_ - 1
        break

print(p1)  # 896
print(p2)  # 659

stop = datetime.now()
print("duration:", stop - start)