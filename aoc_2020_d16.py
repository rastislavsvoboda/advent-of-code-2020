from datetime import datetime
from datetime import timedelta
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
                # if at least num if in defined intervals, ticket is valid
                is_valid = True
                break
        if not is_valid:
            # add num that is not valid for any range
            s += n
    return s


def possible_assign(rules, ticket):
    res = []
    for n in ticket:
        # compute all rules names that n is in defined ranges
        possible = set()
        for name, (min1, max1, min2, max2) in rules.items():
            if min1 <= n <= max1 or min2 <= n <= max2:
                possible.add(name)
        res.append(possible)
    return res


def solve(text):
    data = get_data(text)
    # print(data)
    rules = parse_rules(data[0])
    your_ticket = parse_your_ticket(data[1])
    nearby_tickers = parse_nearby_tickets(data[2])

    res1 = 0
    # get possible assignments for valid tickets
    possible_assignments = []
    for t in nearby_tickers:
        validity_sum = valid_sum(rules, t)
        res1 += validity_sum
        if validity_sum == 0:
            possible_assignments.append(possible_assign(rules, t))

    # intersect possible results for per column
    intersected_results = []
    for i in range(len(rules)):
        possibilities = set(rules.keys())
        for poss in possible_assignments:
            possibilities = possibilities.intersection(poss[i])
        intersected_results.append(possibilities)

    # find final assignments for columns
    # iteratively remove when there is just one possibility
    final_assignments = {}
    while len(final_assignments) < len(rules):
        matched = None
        for i, poss in enumerate(intersected_results):
            if len(poss) == 1:
                # just 1 possiblity, so this is final
                matched = poss.pop()
                final_assignments[matched] = i
                break
        if matched:
            # remove matched from others
            for poss in intersected_results:
                if matched in poss:
                    poss.remove(matched)

    # multiple all values for 'departure *' values
    res2 = 1
    for k, v in final_assignments.items():
        if k.startswith("departure"):
            res2 *= your_ticket[v]        

    return res1, res2


print(solve(text)) # 26980, 3021381607403

stop = datetime.now()
print("duration:", stop - start)