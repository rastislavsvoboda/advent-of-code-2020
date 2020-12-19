from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import sys
import copy
import re
import time

# .\get.ps1 19

start = datetime.now()
text = open('19.in').read()

TCHAR = 1
TLST = 2
TOR = 3

def parse(text):
    data = []
    for grp in text.split('\n\n'):
        data.append(grp.split('\n'))    
    rules = parse_rules(data[0])
    messages = data[1]
    return (rules, messages)


def parse_rules(text):
    rules = {}
    head = []
    for line in text:
        line = line.strip()
        if not line:
            continue

        # cannot do this - infinite recursion
        # if not p1:
        #     if str.startswith(line, '8:'):
        #         line = "8: 42 | 42 8"
        #     if str.startswith(line, '11:'):
        #         line = "11: 42 31 | 42 11 31"

        parts = line.split(':')
        name = int(parts[0])
        if "a" in parts[1]:
            rules[name] = (TCHAR, "a")
            head.append(name)
        elif "b" in parts[1]:
            rules[name] = (TCHAR, "b")
            head.append(name)
        elif "|" in parts[1]:
            ored = parts[1].split('|')
            nums1 = [int(n) for n in re.findall(r'\d+', ored[0])]
            nums2 = [int(n) for n in re.findall(r'\d+', ored[1])]
            rules[name] = (TOR, (nums1, nums2))
        else:
            nums = [int(n) for n in re.findall(r'\d+', parts[1])]
            rules[name] = (TLST, nums)
    return rules


def add_char(acc, x):
    res = []
    for a in acc:
        res.append(a + x)
    return res


def add_list(acc, lst):
    res = []
    for a in acc:
        for x in lst:
            res.append(a + x)
    return res


def eval_rule(rules, r, acc):
    (r_type, r_data) = rules[r]
    if r_type == TCHAR:
        return add_char(acc, r_data)
    elif r_type == TLST:
        res = acc[:]
        for l in r_data:
            res = add_list(res, eval_rule(rules, l, acc))
        return res
    elif r_type == TOR:
        (l1, l2) = r_data
        r1 = acc[:]
        for l in l1:
            r1 = add_list(r1, eval_rule(rules, l, acc))
        r2 = acc[:]
        for l in l2:
            r2 = add_list(r2, eval_rule(rules, l, acc))
        return r1 + r2 # list concat
    assert False


def solve1(data):
    res = 0
    rules, messages = data

    x42 = eval_rule(rules, 42, [""])
    x31 = eval_rule(rules, 31, [""])

    l42 = len(x42[0])
    l31 = len(x31[0])
    assert l42 == l31, "length should match"
    l = l42

    for m in messages:
        if not m:
            continue
        assert len(m) % l == 0
        is_in_42 = [False for i in range(len(m) // l)]
        is_in_31 = [False for i in range(len(m) // l)]

        i = 0
        for indx in range(0, len(m), l):
            if m[indx:indx + l] in x42:
                is_in_42[i] = True
            if m[indx:indx + l] in x31:
                is_in_31[i] = True
            i += 1

        # fast - hardcoded for rule 0: -> 8 | 11 -> 42 42 31
        if len(is_in_42) == len(is_in_31) == 3:
            if is_in_42[0] == True and is_in_42[1] == True and is_in_31[2] == True:
                res +=1

    return res


def solve2(data):
    res = 0
    rules, messages = data

    x42 = eval_rule(rules, 42, [""])
    # print("42: ", len(x42))
    x31 = eval_rule(rules, 31, [""])
    # print("31: ", len(x31))

    l42 = len(x42[0])
    l31 = len(x31[0])
    assert l42 == l31, "length should match"
    l = l42

    for m in messages:
        if not m:
            continue
        assert len(m) % l == 0
        is_in_42 = [False for i in range(len(m) // l)]
        is_in_31 = [False for i in range(len(m) // l)]

        i = 0
        for indx in range(0, len(m), l):
            if m[indx:indx + l] in x42:
                is_in_42[i] = True
            if m[indx:indx + l] in x31:
                is_in_31[i] = True
            i += 1

        b = 0 if is_in_42[0] else -1
        e = len(is_in_31) - 1 if is_in_31[-1] else len(is_in_31)

        while b >= 0 and b < len(is_in_42) and is_in_42[b] == True:
            b += 1

        while e >= 0 and e < len(is_in_31) and is_in_31[e] == True:
            e -= 1

        if b == e + 1:
            # print("ok", m)
            assert b >= 0
            assert e < len(is_in_31)
            # assert b>=len(is_in_42)//2, "wrong b"
            if b > len(is_in_42) // 2:
                res += 1
                # print("b", b)
            # else:
            #     print(is_in_42)
            #     print(is_in_31)
            #     print("not ok")
        # print("****")

    return res

data = parse(text)
print(solve1(data))  # 142
print(solve2(data))  # 294
# p2: wrong 343, 329, 313 too high

stop = datetime.now()
print("duration:", stop - start)