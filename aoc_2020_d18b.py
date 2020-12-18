from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 18

start = datetime.now()
lines = open('18.in').readlines()


def rec_eval(indx, line, p1):
    q = deque()
    # parse to queue
    while indx < len(line):
        c = line[indx]
        if c == "(":
            sub_eval, indx = rec_eval(indx + 1, line, p1)
            q.append(sub_eval)
        elif c == ")":
            indx += 1
            break
        elif str.isdigit(c):
            q.append(int(c))
            indx += 1
        elif c == '+' or c == '*':
            q.append(c)
            indx += 1
        elif c == ' ':
            indx += 1
    # evaluate
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
                    q_skipp = deque()
                    while (op == "*"):
                        q_skipp.append(n1)
                        q_skipp.append(op)
                        n1 = n2
                        op = q.popleft()
                        n2 = q.popleft()
                    assert op == "+", "op should be +"
                    q.appendleft(n1 + n2)
                    while q_skipp:
                        q.appendleft(q_skipp.pop())
        else:
            assert False, F"wrong op:{op}"
    assert len(q) == 1, "q should have just 1 item left"
    # get single val as result
    res = q.pop()
    return res, indx


def solve(lines, p1):
    res = 0
    for line in lines:
        line = "(" + line.strip() + ")"
        x, _ = rec_eval(0, line, p1)
        # print(x)
        res += x
    return res


print(solve(lines, True))  # 98621258158412
print(solve(lines, False))  # 241216538527890

stop = datetime.now()
print("duration:", stop - start)