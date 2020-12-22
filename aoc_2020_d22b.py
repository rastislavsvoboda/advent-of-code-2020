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
            if row and not str.startswith(row, 'Player'):
                entries.append(int(row))
        data.append(entries)
    assert len(data) == 2
    assert len(data[0]) == len(data[1])
    return data[0], data[1]


def game(g, p1, p2, part1):
    g_num = g[0]
    r_num = 1
    q1 = deque(p1)
    q2 = deque(p2)
    hist = set()
    while q1 and q2:
        # print(F"round {r_num} (game {g_num})")
        # print(q1)
        # print(q2)
        # print("------")
        if not part1:
            state = (tuple(q1), tuple(q2))
            if state in hist:
                # repeating: winner is player1
                return (True, q1)
            hist.add(state)

        n1 = q1.popleft()
        n2 = q2.popleft()

        if not part1 and (len(q1) >= n1 and len(q2) >= n2):
            # next sub-game
            g[0] += 1
            sub_p1 = list(q1)[:n1]
            sub_p2 = list(q2)[:n2]
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