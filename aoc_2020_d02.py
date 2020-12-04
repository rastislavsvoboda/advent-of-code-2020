from datetime import datetime
from datetime import timedelta
import time

start = datetime.now()
lines = open('2.in').readlines()


def is_valid1(min_occ, max_occ, character, password):
    occ = 0
    for c in password:
        if c == character:
            occ = occ + 1
    return min_occ <= occ <= max_occ


def is_valid2(pos1, pos2, character, password):
    p1_ok = password[pos1 - 1] == character
    p2_ok = password[pos2 - 1] == character
    return p1_ok ^ p2_ok # xor, for bool should work also p1_ok != p2_ok


def solve1(lines):
    res = 0
    for line in lines:
        words = line.strip().split()
        n1, n2 = words[0].split('-')
        min_occ = int(n1)
        max_occ = int(n2)
        character = words[1][0]
        password = words[2]
        if is_valid1(min_occ, max_occ, character, password):
            res = res + 1
    return res


def solve2(lines):
    res = 0
    for line in lines:
        words = line.strip().split()
        n1, n2 = words[0].split('-')
        pos1 = int(n1)
        pos2 = int(n2)
        character = words[1][0]
        password = words[2]
        if is_valid2(pos1, pos2, character, password):
            res = res + 1
    return res


# print(is_valid2(1,3,"c","abcde"))
# print(is_valid2(1,3,"b","invalid"))
# print(is_valid2(2,9,"c","ccccccccc"))

print(solve1(lines))  # 582
print(solve2(lines))  # 729

stop = datetime.now()
print("duration:", stop - start)