from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 5

start = datetime.now()

# s.translate({ord('F'):ord('0'),ord('B'):ord('1'),ord('L'):ord('0'),ord('R'):ord('1')})
S = set(int(s.translate({70: 48,66: 49,76: 48,82: 49}), 2) for s in open("5.in"))
print(max(S), (set(range(min(S), max(S))) - S).pop())  # 896 659

# high = max(S)
# low = min(S)
# print((high * (high + 1) / 2 - (low - 1) * low / 2) - sum(S))

# print(max(S), (sum(range(min(S), max(S)+1)) - sum(S)))  # 896 659


stop = datetime.now()
print("duration:", stop - start)