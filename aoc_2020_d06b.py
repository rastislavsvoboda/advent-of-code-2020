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
    qst = set()
    lines_cnt = len(lines)
    for i, line in enumerate(lines):
        line = line.strip()
        if line:
            for q in line:
                qst.add(q)

        if (not line) or (i == lines_cnt - 1):
            res += len(qst)
            qst = set()

    return res


def solve2(lines):
    res = 0
    group_answers = []
    lines_cnt = len(lines)
    all_questions = set()
    for i, line in enumerate(lines):
        line = line.strip()
        if line:
            for q in line:
                all_questions.add(q)
            group_answers.append(set(line))

        if (not line) or (i == lines_cnt - 1):
            people_cnt = len(group_answers)

            for qst in all_questions:
                answered_qst_cnt = 0
                for ans in group_answers:
                    if qst in ans:
                        answered_qst_cnt += 1
                if answered_qst_cnt == people_cnt:
                    # if all people answered to given question
                    res += 1

            group_answers = []
            all_questions = set()

    return res


print(solve1(lines))  # 6930
print(solve2(lines))  # 3585

stop = datetime.now()
print("duration:", stop - start)