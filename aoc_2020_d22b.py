from datetime import datetime
from collections import deque

# .\get.ps1 22

start = datetime.now()
text = open('22.in').read()


def get_players(text):
    p1, p2 = text.strip('\n').split('\n\n')
    parse = lambda p: list(map(int, p.split('\n')[1:]))
    return parse(p1), parse(p2)


def game(g, p1, p2, part1):
    g_num = g[0]
    r_num = 1
    d1 = deque(p1)
    d2 = deque(p2)
    hist = set()
    while d1 and d2:
        # print(F"round {r_num} (game {g_num})")
        # print(d1)
        # print(d2)
        # print("------")
        if not part1:
            state = (tuple(d1), tuple(d2))
            if state in hist:
                # repeating: winner is player1
                return (True, d1)
            hist.add(state)

        n1 = d1.popleft()
        n2 = d2.popleft()

        if not part1 and (len(d1) >= n1 and len(d2) >= n2):
            # next sub-game
            g[0] += 1
            sub_p1 = list(d1)[:n1]
            sub_p2 = list(d2)[:n2]
            p1_wins, _ = game(g, sub_p1, sub_p2, part1)
        else:
            # higher wins
            p1_wins = n1 > n2

        if p1_wins:
            # print("p1 wins")
            d1.append(n1)
            d1.append(n2)
        else:
            # print("p2 wins")
            d2.append(n2)
            d2.append(n1)
        r_num += 1

    return (True, d1) if d1 else (False, d2)


def solve(player1, player2, part1):
    winner, deck = game([1], player1, player2, part1)
    score = sum([(i + 1) * c for i, c in enumerate(reversed(deck))])
    return score


player1, player2 = get_players(text)
print(solve(player1, player2, True))  # 29764
print(solve(player1, player2, False))  # 32588

stop = datetime.now()
print("duration:", stop - start)