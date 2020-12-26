from datetime import datetime
import functools
import operator

# .\get.ps1 3

start = datetime.now()
lines = open('3.in').readlines()


def parse(line):
    return list(line.strip())


def items(entries, slope):
    dc, dr = slope
    r = dr
    c = dc
    while r < len(entries):
        yield entries[r][c % len(entries[r])]
        r += dr
        c += dc


entries = list(map(parse, lines))
counter = lambda slope: len([c for c in items(entries, slope) if c == "#"])

slope = (3, 1)
res1 = counter(slope)
print(res1)  # 292

# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
cnts = map(counter, slopes)
res2 = functools.reduce(operator.mul, cnts)
print(res2)  # 9354744432

stop = datetime.now()
print("duration:", stop - start)