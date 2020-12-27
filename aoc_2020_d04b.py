from datetime import datetime
from datetime import timedelta
import re
import time

# .\get.ps1 4

start = datetime.now()
text = open('4.in').read()


def get_data(text):
    for grp in text.split('\n\n'):
        entries = [ row for row in grp.split() ]
        yield parse_entry(entries)

def parse_entry(entries):
    return { k:v for k,v in [entry.split(':') for entry in entries] }


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
    if hgt.group(2) == "cm" and not in_range(hgt.group(1), 150, 193):
        return False
    if hgt.group(2) == "in" and not in_range(hgt.group(1), 59, 76):
        return False
    return True


def solve(valid_fn, data):
    return len(list(filter(valid_fn, data)))


data = list(get_data(text))
print(solve(is_valid1, data))  # 219
print(solve(is_valid2, data))  # 127

stop = datetime.now()
print("duration:", stop - start)