from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 25

start = datetime.now()
lines = open('25.in').readlines()


def get_loopsize(subj, key, divider):
    val = 1
    i = 0
    while val != key:
        i += 1
        val *= subj
        val %= divider
    return i


def get_encryption_key(public_key, loop_size, divider):
    val = 1
    subj = public_key
    for _ in range(loop_size):
        val *= subj
        val %= divider
    return val


def solve(lines):
    card_pk = int(lines[0].strip())
    door_pk = int(lines[1].strip())

    # sample
    # card_pk = 5764801
    # door_pk = 17807724

    divider = 20201227

    subj = 7
    card_ls = get_loopsize(subj, card_pk, divider)
    print("card loop size", card_ls)

    door_ls = get_loopsize(subj, door_pk, divider)
    print("door loop size", door_ls)

    enc_key1 = get_encryption_key(card_pk, door_ls, divider)
    enc_key2 = get_encryption_key(door_pk, card_ls, divider)

    assert enc_key1 == enc_key2
    res = enc_key1
    return res


print(solve(lines))  # 12285001

stop = datetime.now()
print("duration:", stop - start)