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
            opts = parts[1].split('|')
            nums1 = [int(n) for n in re.findall(r'\d+', opts[0])]
            nums2 = [int(n) for n in re.findall(r'\d+', opts[1])]
            rules[name] = (TLST, [nums1, nums2])
        else:
            nums = [int(n) for n in re.findall(r'\d+', parts[1])]
            rules[name] = (TLST, [nums])
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
        total = []
        for lsts in r_data:
            res = acc[:]
            for l in lsts:
                res = add_list(res, eval_rule(rules, l, acc))
            total += res
        return total
    assert False


def solve1(data):
    res = 0
    rules, messages = data

    r42 = eval_rule(rules, 42, [""])
    r31 = eval_rule(rules, 31, [""])

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

        # fast - hardcoded for rule 0: -> 8 | 11 -> 42 42 31
        if len(is_in_42) == len(is_in_31) == 3:
            if is_in_42[0] and is_in_42[1] and is_in_31[2]:
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

        # b = 0 if is_in_42[0] else -1 # first must be 42
        # e = len(is_in_31) - 1 if is_in_31[-1] else len(is_in_31) # last must be 31

        # while 0 <= b < len(is_in_42) and is_in_42[b]:
        #     b += 1

        # while 0 <= e < len(is_in_31) and is_in_31[e]:
        #     e -= 1

        # if b == e + 1:
        #     # begin and end should just "cross"
        #     assert 0 <= b
        #     assert e < len(is_in_31)
        #     if b > len(is_in_42) // 2:
        #         # 42 must be more times than 31
        #         # because 0: 8 11
        #         # because 8: 42 | 42 8
        #         # because 11: 42 11 31
        #         # so min possibility is 42 42 31
        #         # next: 42 .... 42 42 31 31
        #         res += 1

        # hopefully better
        cnt42 = 0
        cnt31 = 0
        i = 0
        if is_in_42[i]:
            cnt42 += 1
            i += 1
            while i < len(is_in_42) and is_in_42[i]:
                cnt42 += 1
                i += 1
            while i < len(is_in_31) and is_in_31[i]:
                cnt31 += 1
                i += 1
            if i == len(is_in_31) and 0 < cnt31 < cnt42:
                res += 1

    return res


data = parse(text)
print(solve1(data))  # 142
print(solve2(data))  # 294
# p2: wrong 343, 329, 313 too high

stop = datetime.now()
print("duration:", stop - start)