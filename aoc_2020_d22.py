from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 22

start = datetime.now()
text = open('22.in').read()


def get_players(text):
    data = []
    for grp in text.split('\n\n'):
        entries = []
        for row in grp.split('\n'):
            if row:
                entries.append(row)
        data.append(entries)
    # skip player's label and convert to numbers
    p1 = [int(x) for x in data[0][1:]]
    p2 = [int(x) for x in data[1][1:]]
    assert len(p1) == len(p2)
    return p1, p2


def game1(p1, p2):
    q1 = deque(p1)
    q2 = deque(p2)
    r = 1
    while q1 and q2:
        # print("round ", r)
        # print(q1)
        # print(q2)
        # print("------")
        n1 = q1.popleft()
        n2 = q2.popleft()
        # bigger wins
        if n1 > n2:
            q1.append(n1)
            q1.append(n2)
            # print("p1 wins")
        elif n2 > n1:
            q2.append(n2)
            q2.append(n1)
            # print("p2 wins")
        else:
            assert False, "draw"
        r += 1

    if q1:
        return True, q1
    else:
        return False, q2


def score(result):
    _, q = result
    l = len(q)
    score = 0
    for i, c in enumerate(q):
        score += (l - i) * c
    return score


def game2(g, p1, p2):
    game = g[0]
    r = 1
    q1 = deque(p1)
    q2 = deque(p2)
    hist1 = set()
    hist2 = set()
    while q1 and q2:
        # print(F"round {r} (game {game})")
        # print(q1)
        # print(q2)
        # print("------")
        curr1 = tuple(list(q1))
        curr2 = tuple(list(q2))

        if curr1 in hist1 or curr2 in hist2:
            # repeating: winner is player1
            return (True, q1)

        hist1.add(curr1)
        hist2.add(curr2)

        n1 = q1.popleft()
        n2 = q2.popleft()

        if n1 <= len(curr1) - 1 and n2 <= len(curr2) - 1:
            # next sub-game
            g[0] += 1
            sub_p1 = [c for c in list(curr1)[1:n1 + 1]]
            sub_p2 = [c for c in list(curr2)[1:n2 + 1]]
            p1_wins, _ = game2(g, sub_p1, sub_p2)
            if p1_wins:
                q1.append(n1)
                q1.append(n2)
            else:
                q2.append(n2)
                q2.append(n1)
        else:
            # bigger wins
            if n1 > n2:
                q1.append(n1)
                q1.append(n2)
                # print("p1 wins")
            elif n2 > n1:
                q2.append(n2)
                q2.append(n1)
                # print("p2 wins")
        r += 1

    if q1:
        return True, q1
    else:
        return False, q2





def solve(player1, player2, part1):
    if part1:
        return score(game1(player1, player2))
    else:
        return score(game2([1, 1], player1, player2))


player1, player2 = get_players(text)
print(solve(player1, player2, True))  # 29764
print(solve(player1, player2, False))  # 32588

stop = datetime.now()
print("duration:", stop - start)