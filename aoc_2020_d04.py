from datetime import datetime
from datetime import timedelta
import re
import time

# .\get.ps1 4

start = datetime.now()
lines = open('4.in').readlines()


def is_valid1(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    keys = passport.keys()
    for req in required:
        if req not in keys:
            return False
    return True


def in_range(val, minval, maxval):
    return (minval <= int(val) <= maxval)


def is_valid2(passport):
    if not is_valid1(passport):
        return False
    if not in_range(passport['byr'], 1920, 2002):
        return False
    if not in_range(passport['iyr'], 2010, 2020):
        return False
    if not in_range(passport['eyr'], 2020, 2030):
        return False
    if not re.match(r"#[0-9a-f]{6}", passport['hcl']):
        return False
    if not re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']):
        return False
    if not re.match(r"^\d{9}$", passport['pid']):
        return False

    hgt = re.match(r"^(\d+)(cm|in)$", passport['hgt'])
    if not hgt:
        return False
    if hgt.group(2) == "cm":
        if not in_range(hgt.group(1), 150, 193):
            return False
    elif hgt.group(2) == "in":
        if not in_range(hgt.group(1), 59, 76):
            return False
    else:
        return False

    return True


def solve(lines, part):
    res = 0
    passport = {}
    lines_cnt = len(lines)
    for i, line in enumerate(lines):
        line = line.strip()

        if line:
            words = line.split()
            for w in words:
                k, v = w.split(':')
                passport[k] = v

        if (not line) or (i == lines_cnt - 1):
            if part == 1:
                if is_valid1(passport):
                    res += 1
            elif part == 2:
                if is_valid2(passport):
                    res += 1

            passport = {}

    return res


print(solve(lines, 1))  # 219
print(solve(lines, 2))  # 127

stop = datetime.now()
print("duration:", stop - start)