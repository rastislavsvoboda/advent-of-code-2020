from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import functools
import copy
import re
import time

# .\get.ps1 10

start = datetime.now()
lines = open('10.in').readlines()


def solve1(lines):
    adapters = [int(x) for x in lines]
    sorted_adapters = list(sorted(adapters))

    device_jolts = max(adapters) + 3
    sorted_adapters.append(device_jolts)

    current = 0
    diff1 = 0
    diff3 = 0
    for i, n in enumerate(sorted_adapters):
        if current + 1 == n:
            diff1 += 1
            current = n
        elif current + 3 == n:
            diff3 += 1
            current = n

        if current >= device_jolts:
            break

    return diff1 * diff3


def get_compatible(adapters, joltage):
    compatible = []
    if joltage + 1 in adapters:
        compatible.append(joltage + 1)
    if joltage + 2 in adapters:
        compatible.append(joltage + 2)
    if joltage + 3 in adapters:
        compatible.append(joltage + 3)
    return compatible


def solve2(lines):
    adapters = [int(x) for x in lines]
    sorted_adapters = list(sorted(adapters))

    outlet_jolts = 0
    sorted_adapters.insert(0, outlet_jolts)
    device_jolts = max(adapters) + 3
    sorted_adapters.append(device_jolts)

    # inspired from internet
    compatible = {}
    for jolt in sorted_adapters[:-1]:
        compatible[jolt] = get_compatible(sorted_adapters, jolt)

    numArrange = {sorted_adapters[-1]: 1}
    for jolt in reversed(sorted_adapters[:-1]):
        numArrange[jolt] = sum(numArrange[j] for j in compatible[jolt])

    return numArrange[outlet_jolts]


print(solve1(lines))  # 2310
print(solve2(lines))  # 64793042714624

stop = datetime.now()
print("duration:", stop - start)