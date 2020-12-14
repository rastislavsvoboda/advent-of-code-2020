from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 14

start = datetime.now()
lines = open('14.in').readlines()

p1=0
p2=0

mask = ''
mem={}
for line in lines:
    line = line.strip()
    if line.startswith('mask'):
        newmask = line.split()[-1]
        mask=newmask
    else:
        idx,_,value = line.split()
        idx = int(idx.split('[')[-1][:-1])
        value = int(value)
        newvalue=0
        for i,bit in enumerate(reversed(mask)):
            vbit = value & (2**i)
            if bit == 'X':
                newvalue += vbit
            elif bit == '1':
                newvalue += 2**i
            else:
                pass

        mem[idx] = newvalue

ans = 0
for v in mem.values():
    ans += v

print(ans)


stop = datetime.now()
print("duration:", stop - start)