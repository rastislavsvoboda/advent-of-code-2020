from datetime import datetime
from datetime import timedelta
import re
import time

# .\get.ps1 4

start = datetime.now()
lines = open('4.in').read()


def get_data(lines):
    data = []
    for grp in lines.split('\n\n'):
        entries = []
        for row in grp.split():
            entries.append(row)
        data.append(parse_entry(entries))
    return data


def parse_entry(entries):
    passport = {}
    for entry in entries:
        k, v = entry.split(':')
        passport[k] = v
    return passport


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
    if not re.match(r"^#[0-9a-f]{6}$", passport['hcl']):
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


def solve1(lines):
    return len(list(filter(lambda p: is_valid1(p), get_data(lines))))


def solve2(lines):
    return len(list(filter(lambda p: is_valid2(p), get_data(lines))))


print(solve1(lines))  # 219
print(solve2(lines))  # 127

stop = datetime.now()
print("duration:", stop - start)