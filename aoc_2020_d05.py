from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 5

start = datetime.now()
lines = open('5.in').readlines()


def half(min_val, max_val, ch):
    mid_val = (max_val - min_val + 1) // 2
    if ch in ['F', 'L']:
        # Front or Left moves max
        max_val = max_val - mid_val
    elif ch in ['B', 'R']:
        # Back or Right moves min
        min_val = min_val + mid_val
    else:
        assert False, "unknown char: " + ch
    return (min_val, max_val)


def get_seat_ids(lines):
    seat_ids = []
    for line in lines:
        line = line.strip()

        # first 7 chars: row from 0 - 127
        min_row, max_row = 0, 127
        for r in line[:7]:
            (min_row, max_row) = half(min_row, max_row, r)
        assert min_row == max_row, "wrong row"
        row = min_row

        # next char: columns from 0 - 7
        min_col, max_col = 0, 7
        for c in line[7:]:
            (min_col, max_col) = half(min_col, max_col, c)
        assert min_col == max_col, "wrong column"
        col = min_col

        # formula for seat_id
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
    return seat_ids


def solve1(lines):
    seat_ids = sorted(get_seat_ids(lines), reverse=True)
    # max seat id
    res = seat_ids[0]
    return res


def solve2(lines):
    res = None
    seat_ids = sorted(get_seat_ids(lines))
    sid = seat_ids[0]
    for i in seat_ids[1:]:
        if i != sid + 1:
            # missing next sid
            res = sid + 1
            break
        sid = i
    return res


# def solve2b(lines):
#     res = 0
#     seat_ids = sorted(get_seat_ids(lines))
#     for i in range(seat_ids[0], seat_ids[-1] + 1):
#         if i not in seat_ids:
#             res = i
#             break
#     return res


print(solve1(lines))  # 896
print(solve2(lines))  # 659

stop = datetime.now()
print("duration:", stop - start)