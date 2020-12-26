from datetime import datetime
from datetime import timedelta
import time

start = datetime.now()
lines = open('2.in').readlines()


def parse(l):
    words = l.strip().split()
    n1, n2 = list(map(int, words[0].split('-')))
    character = words[1][0]
    password = words[2]
    return (n1, n2, character, password)


def is_valid1(entry):
    min_occ, max_occ, character, password = entry
    occ = len([c for c in list(password) if c == character])
    return min_occ <= occ <= max_occ


def is_valid2(entry):
    pos1, pos2, character, password = entry
    p1_ok = password[pos1 - 1] == character
    p2_ok = password[pos2 - 1] == character
    return p1_ok ^ p2_ok  # xor, for bool should work also p1_ok != p2_ok


def solve1(lines):
    return len(list(filter(is_valid1, entries)))


def solve2(lines):
    return len(list(filter(is_valid2, entries)))


# print(is_valid2((1,3,"c","abcde")))
# print(is_valid2((1,3,"b","invalid")))
# print(is_valid2((2,9,"c","ccccccccc")))

entries = list(map(parse, lines))
print(solve1(entries))  # 582
print(solve2(entries))  # 729

stop = datetime.now()
print("duration:", stop - start)