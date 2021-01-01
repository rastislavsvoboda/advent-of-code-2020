from datetime import datetime
from datetime import timedelta
import re
import time

# .\get.ps1 4

start = datetime.now()
text = open('4.in').read()


def get_data(text):
    for grp in text.split('\n\n'):
        entries = [row for row in grp.split()]
        yield parse_entry(entries)


def parse_entry(entries):
    return {k: v for k, v in [entry.split(':') for entry in entries]}


def in_range(val, minval, maxval):
    return (minval <= int(val) <= maxval)


def match_hgt(v):
    hgt = re.match(r"^(\d+)(cm|in)$", v)
    if not hgt:
        return False
    if hgt.group(2) == "cm" and not in_range(hgt.group(1), 150, 193):
        return False
    if hgt.group(2) == "in" and not in_range(hgt.group(1), 59, 76):
        return False

    return True


def is_valid1(passport, reqs):
    keys = passport.keys()
    return all(k in keys for k in reqs.keys())


def is_valid2(passport, reqs):
    keys = passport.keys()
    return all((k in keys) and (v(passport[k])) for k, v in reqs.items())


def solve(valid_fn, data, reqs):
    return len(list(filter(lambda p: valid_fn(p, reqs), data)))


reqs = {
    'byr': lambda v: in_range(v, 1920, 2002),
    'iyr': lambda v: in_range(v, 2010, 2020),
    'eyr': lambda v: in_range(v, 2020, 2030),
    'hgt': lambda v: match_hgt(v),
    'hcl': lambda v: re.match(r"^#[0-9a-f]{6}$", v),
    'ecl': lambda v: re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", v),
    'pid': lambda v: re.match(r"^\d{9}$", v)
}

data = list(get_data(text))
print(solve(is_valid1, data, reqs))  # 219
print(solve(is_valid2, data, reqs))  # 127

stop = datetime.now()
print("duration:", stop - start)
