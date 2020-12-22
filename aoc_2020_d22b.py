from datetime import datetime
from collections import deque

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


def game(g, p1, p2, part1):
    g_num = g[0]
    r_num = 1
    q1 = deque(p1)
    q2 = deque(p2)
    hist1 = set()
    hist2 = set()
    while q1 and q2:
        # print(F"round {r_num} (game {g_num})")
        # print(q1)
        # print(q2)
        # print("------")
        if not part1:
            curr1 = tuple(list(q1))
            curr2 = tuple(list(q2))

            if curr1 in hist1 or curr2 in hist2:
                # repeating: winner is player1
                return (True, q1)

            hist1.add(curr1)
            hist2.add(curr2)

        n1 = q1.popleft()
        n2 = q2.popleft()

        if not part1 and (len(q1) >= n1 and len(q2)>= n2):
            # next sub-game
            g[0] += 1
            sub_p1 = [c for c in list(q1)[:n1]]
            sub_p2 = [c for c in list(q2)[:n2]]
            p1_wins, _ = game(g, sub_p1, sub_p2, part1)
        else:
            # higher wins
            p1_wins = n1 > n2

        if p1_wins:
            # print("p1 wins")
            q1.append(n1)
            q1.append(n2)
        else:
            # print("p2 wins")
            q2.append(n2)
            q2.append(n1)
        r_num += 1

    return (True, q1) if q1 else (False, q2)


def solve(player1, player2, part1):
    winner, q = game([1], player1, player2, part1)
    score = sum([(i + 1) * c for i, c in enumerate(reversed(q))])
    return score


player1, player2 = get_players(text)
print(solve(player1, player2, True))  # 29764
print(solve(player1, player2, False))  # 32588

stop = datetime.now()
print("duration:", stop - start)