from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 13

start = datetime.now()
lines = open('13.in').readlines()


def mod_pow(b, e, mod):
    if e == 0:
        return 1
    elif e % 2 == 0:
        return mod_pow((b * b) % mod, e // 2, mod)
    else:
        return (b * mod_pow(b, e - 1, mod)) % mod


def mod_inverse(a, m):
    return mod_pow(a, m - 2, m)


B = lines[1].strip().split(',')
constraints = []
N=1
for i,b in enumerate(B):
    if b!='x':
        b = int(b)
        i %= b
        constraints.append(((b-i)%b,b))
        N*=b

ans = 0
for i,b in constraints:
    NI=N//b
    mi = mod_inverse(NI,b)
    for_b = i*mi*NI
    ans+=for_b

ans %= N

print(ans) # 556100168221141


stop = datetime.now()
print("duration:", stop - start)