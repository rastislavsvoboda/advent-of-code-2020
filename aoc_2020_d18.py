from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 18

start = datetime.now()
lines = open('18.in').readlines()


def eval_queue(q, p1):
    while len(q) >= 3:
        n1 = q.popleft()
        op = q.popleft()
        n2 = q.popleft()
        if op == "+":
            q.appendleft(n1 + n2)
        elif op == "*":
            if p1:
                q.appendleft(n1 * n2)
            else:
                if "+" not in q:
                    q.appendleft(n1 * n2)
                else:
                    q2 = deque()
                    while (op == "*"):
                        q2.append(n1)
                        q2.append(op)
                        n1 = n2
                        op = q.popleft()
                        n2 = q.popleft()
                    q2.append(n1+n2)
                    while q2:
                        x= q2.pop()                
                        q.appendleft(x)
        else:
            assert False, F"wrong op {op}"

def rec_eval(acc, indx, line, p1):
    if indx >= len(line):
        return acc, indx

    s = ""
    n = 0
    q = deque()
    while indx < len(line):
        c = line[indx]
        if c == "(":
            sub_eval, indx = rec_eval(0, indx + 1, line, p1)
            q.append(sub_eval)
        elif c == ")":
            indx += 1
            if s != "":
                n = int(s)
                q.append(n)
                s = ""
                eval_queue(q, p1)
            break
        elif c == ' ':
            if s != "":
                n = int(s)
                q.append(n)
                s = ""
            indx += 1
        elif str.isdigit(c):
            s += c
            indx += 1
        elif c == '+':
            q.append(c)
            indx += 1
        elif c == '*':
            q.append(c)
            indx += 1
        else:
            assert False

    eval_queue(q, p1)

    assert len(q) == 1
    res = q.pop()
    return res, indx


def evaluate(i, line, p1):
    if line == "":
        return 0
    line = "(" + line + ")"
    res, indx = rec_eval(0, 0, line, p1)
    assert indx == len(line)
    return res


def solve(lines, p1):
    res = 0
    for line in lines:
        line = line.strip()
        x = evaluate(0,line, p1)
        # print(x)
        res += x
    return res


print(solve(lines, True))  # 98621258158412
print(solve(lines, False))  # 241216538527890

stop = datetime.now()
print("duration:", stop - start)