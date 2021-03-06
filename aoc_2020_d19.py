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
        elif "b" in parts[1]:
            rules[name] = (TCHAR, "b")
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
    r0 = eval_rule(rules, 0, [""])
    for msg in messages:
        if not msg:
            continue
        # print(msg)
        if msg in r0:
            res += 1
    return res


def solve2(data):
    res = 0
    rules, messages = data

    r42 = eval_rule(rules, 42, [""])
    # print("42: ", len(r42))
    r31 = eval_rule(rules, 31, [""])
    # print("31: ", len(r31))

    l42 = len(r42[0])
    l31 = len(r31[0])
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
            if m[indx:indx + l] in r42:
                is_in_42[i] = True
            if m[indx:indx + l] in r31:
                is_in_31[i] = True
            i += 1

        b = 0 if is_in_42[0] else -1 # first must be 42
        e = len(is_in_31) - 1 if is_in_31[-1] else len(is_in_31) # last must be 31

        while 0 <= b < len(is_in_42) and is_in_42[b]:
            b += 1

        while 0 <= e < len(is_in_31) and is_in_31[e]:
            e -= 1

        if b == e + 1:
            # begin and end should just "cross"
            assert 0 <= b
            assert e < len(is_in_31)
            if b > len(is_in_42) // 2:
                # 42 must be more times than 31
                # because 0: 8 11
                # because 8: 42 | 42 8
                # because 11: 42 11 31
                # so min possibility is 42 42 31
                # next: 42 .... 42 42 31 31
                res += 1

    return res

data = parse(text)
print(solve1(data))  # 142
print(solve2(data))  # 294
# p2: wrong 343, 329, 313 too high

stop = datetime.now()
print("duration:", stop - start)