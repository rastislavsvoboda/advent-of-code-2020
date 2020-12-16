from datetime import datetime
from datetime import timedelta
import functools
import copy
import re
import time

# .\get.ps1 16

start = datetime.now()
text = open('16.in').read()


def get_data(text):
    data = []
    for grp in text.split('\n\n'):
        data.append(grp.split('\n'))
    return data


def parse_rules(data):
    rules = {}
    for line in data:
        parts = line.split(':')
        name = parts[0]
        nums = [int(n) for n in re.findall(r'\d+', parts[1])]
        assert len(nums) == 4
        # print(name, nums)
        rules[name] = nums
    return rules


def parse_your_ticket(lines):
    assert lines[0] == "your ticket:"
    ticket = [int(n) for n in lines[1].split(',')]
    # print(ticket)
    return ticket


def parse_nearby_tickets(lines):
    assert lines[0] == "nearby tickets:"
    tickets = []
    for line in lines[1:]:
        if line:
            ticket = [int(n) for n in line.split(',')]
            tickets.append(ticket)
    # print(tickets)
    return tickets


def valid_sum(rules, ticket):
    s = 0
    for n in ticket:
        is_valid = False
        for k, (min1, max1, min2, max2) in rules.items():
            if min1 <= n <= max1 or min2 <= n <= max2:
                # if at least num is in defined intervals, ticket is valid
                is_valid = True
                break
        if not is_valid:
            # add num that is not valid for any range
            s += n
    return s


def solve1(text):
    res = 0
    data = get_data(text)
    # print(data)
    rules = parse_rules(data[0])
    your_ticket = parse_your_ticket(data[1])
    nearby_tickers = parse_nearby_tickets(data[2])
    for t in nearby_tickers:
        res += valid_sum(rules, t)
    return res


def possible_assign(rules, ticket):
    res = []
    for n in ticket:
        # collect all rule names that n is in defined ranges
        possible = set()
        for name, (min1, max1, min2, max2) in rules.items():
            if min1 <= n <= max1 or min2 <= n <= max2:
                possible.add(name)
        res.append(possible)
    return res


def get_assignments(rules, nearby_tickets):
    possible_assignments = [set(rules.keys()) for _ in range(len(rules))]
    for t in nearby_tickets:
        if valid_sum(rules, t) != 0:
            continue # skip invalid
        poss_assign = possible_assign(rules, t)
        for i in range(len(rules)):
            possible_assignments[i] &= poss_assign[i] # intersect

    # find final assignments: iteratively remove when there is just one possibility
    final_assignments = {}
    while len(final_assignments) < len(rules):
        for i, poss_assign in enumerate(possible_assignments):
            if len(poss_assign) == 1:
                # just 1 possiblity, so this is final
                matched = poss_assign.pop()
                assert matched not in final_assignments
                final_assignments[matched] = i
                # remove matched from others
                for pa in possible_assignments:
                    if matched in pa:
                        pa.remove(matched)
                break
    return final_assignments


def solve2(text):
    data = get_data(text)
    # print(data)
    rules = parse_rules(data[0])
    your_ticket = parse_your_ticket(data[1])
    nearby_tickets = parse_nearby_tickets(data[2])
    assignments = get_assignments(rules, nearby_tickets)
    res = 1
    for k, v in assignments.items():
        if k.startswith("departure"):
            res *= your_ticket[v]
    return res


print(solve1(text))  # 26980
print(solve2(text))  # 3021381607403

stop = datetime.now()
print("duration:", stop - start)