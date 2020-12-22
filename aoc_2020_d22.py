from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 22

start = datetime.now()
# lines = open('22.in').readlines()
text = open('22.in').read()


def get_data(text):
    data = []
    for grp in text.split('\n\n'):
        entries = []
        for row in grp.split('\n'):
            entries.append(row)
        data.append(entries)
    return data


def serial(l):


    r =  ",".join([str(x) for x in l])
    return r


def snapshot(q):
    s = []
    q2 = copy.deepcopy(q)
    while q2:
        s.append(q2.popleft())
    return tuple(s)


def game(g, p1, p2):
    q1 = deque()
    q2 = deque()

    for n1 in p1:
        q1.append(n1)

    for n2 in p2:
        q2.append(n2)

    r = 1
    winner = None
    h1 = set()
    h2 = set()
    while q1 and q2:
        # print(F"round {r} (game {g})")
        # print(q1)
        # print(q2)
        # print("------")
        cur1 = snapshot(q1)
        cur2 = snapshot(q2)

        # s1 = serial(cur1)
        # s2 = serial(cur2)

        if cur1 in h1 or cur2 in h2:
            winner = 1
            return (winner, q1, q2)

        h1.add(cur1)
        h2.add(cur2)


        n1 = q1.popleft()
        n2 = q2.popleft()


        if n1 <= len(cur1)-1 and n2 <= len(cur2)-1:
            sub_p1 = [c for c in list(cur1)[1:n1+1]]
            sub_p2 = [c for c in list(cur2)[1:n2+1]]
            w,_,_ = game(g+1, sub_p1, sub_p2)
            if w == 1:
                q1.append(n1)
                q1.append(n2)
            elif w ==2:
                q2.append(n2)   
                q2.append(n1)
            else:
                assert False, "draw"
        else:
            if n1>n2:
                q1.append(n1)
                q1.append(n2)
                # print("p1 wins")
            elif n2>n1:
                q2.append(n2)   
                q2.append(n1)
                # print("p2 wins")
            else:
                assert False, "draw"

        r+=1

    winner = 1 if q1 else 2
    return (winner, q1, q2)

def solve1(text):
    res = 0
    
    data = get_data(text)
    p1 = data[0]
    p2 = data[1]

    p1 = [int(x) for x in p1[1:]]    
    p2 = [int(x) for x in p2[1:-1]]    

    assert len(p1) == len(p2)
    n = len(p1)

    q1 = deque()
    q2 = deque()
    for n1,n2 in zip(p1,p2):
        q1.append(n1)
        q2.append(n2)

    r = 1
    while q1 and q2:
        # print("round ", r)
        # print(q1)
        # print(q2)
        # print("------")
        n1 = q1.popleft()
        n2 = q2.popleft()
        if n1>n2:
            q1.append(n1)
            q1.append(n2)
            # print("p1 wins")
        elif n2>n1:
            q2.append(n2)
            q2.append(n1)
            # print("p2 wins")
        else:
            assert False, "draw"
        r+=1

    # print(q1)
    # print(q2)
        
    sc1 = 0
    i = 1    
    while q1:
        n = q1.pop()
        sc1 += (i * n)
        i+=1

    sc2 = 0
    i = 1    
    while q2:
        n = q2.pop()
        sc2 += (i * n)
        i+=1

    if sc1>0:
        res = sc1
    elif sc2>0:
        res = sc2
    else:
        res = None

    return res

def solve2(text):
    res = 0
    
    data = get_data(text)
    p1 = data[0]
    p2 = data[1]

    p1 = [int(x) for x in p1[1:]]    
    p2 = [int(x) for x in p2[1:-1]]    

    # print(p1)
    # print(p2)

    assert len(p1) == len(p2)
    n = len(p1)


    w,q1,q2 = game(1, p1, p2)

    p1_score=0
    p2_score=0


        

    sc1 = 0
    i = 1    
    while q1:
        n = q1.pop()
        sc1 += (i * n)
        i+=1

    sc2 = 0
    i = 1    
    while q2:
        n = q2.pop()
        sc2 += (i * n)
        i+=1

    if sc1>0:
        res = sc1
    elif sc2>0:
        res = sc2
    else:
        res = None

    return res


print(solve1(text))  # 29764
print(solve2(text))  # 32588

stop = datetime.now()
print("duration:", stop - start)