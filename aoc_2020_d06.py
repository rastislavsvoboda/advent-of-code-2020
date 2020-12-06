from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 6

start = datetime.now()
lines = open('6.in').readlines()


def solve1(lines):
    res = 0

    freqs = defaultdict(int) 
    lines_cnt = len(lines)
    for i, line in enumerate(lines):
    # for i,line in lines:
        line = line.strip()
        if line:
            answers = list(line)
            for ch in answers:
                freqs[ch] += 1
        
        if (not line) or (i == lines_cnt - 1):
            print(freqs)
            print("len: " , len(freqs))
            print(line)

            res += len(freqs)
            freqs = defaultdict(int)

    return res

def solve2(lines):
    res = 0

    lines_cnt = len(lines)

    people=[]

    for i, line in enumerate(lines):
    # for i,line in lines:
        line = line.strip()
        if line:

            freqs = defaultdict(int) 
            answers = list(line)
            for ch in answers:
                freqs[ch] += 1
            people.append(freqs)
        
        if (not line) or (i == lines_cnt - 1):
            # print(people)
            # print(freqs)
            # print("len: " , len(freqs))
            # print(line)

            p_cnt = len(people)

            qst = set()
            for p in people:
                for k in p.keys():
                    qst.add(k)

            for q in qst:
                cnt = 0
                for p in people:
                    if q in p:
                        cnt += 1                  
                if cnt == len(people):
                    res += 1


            # res += len(freqs)
            # freqs = defaultdict(int)
            people = []

    return res




print(solve1(lines))  # 6930
print(solve2(lines))  # 3585

stop = datetime.now()
print("duration:", stop - start)