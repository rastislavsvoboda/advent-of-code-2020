from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 24

start = datetime.now()
lines = open('24.in').readlines()


def get_tile_pos(line):
    x,y = 0,0
    i=0
    while i < len(line+" "):
        c = line[i:i+1]
        cc = line[i:i+2]
        if c == "w":
            x -= 2
            i+=1
        elif c == "e":
            x += 2
            i+=1
        elif cc == "nw":
            x -=1 
            y -=1
            i+=2
        elif cc == "se":
            x +=1 
            y +=1
            i+=2
        elif cc == "ne":
            x +=1 
            y -=1
            i+=2
        elif cc == "sw":
            x -=1 
            y +=1
            i+=2
        elif c == ' ' or c == '':
            break
    return (x,y)



def solve1(lines):
    res = 0

    T = {}

    for line in lines:
        line = line.strip()
        # print(line)
        pos = get_tile_pos(line)
        tile = T.get(pos, "w")
        if tile == "w":
            T[pos] = "b"
        else:
            T[pos] = "w"


    for k,v in T.items():
        if v == "b":
            res += 1

    return res

def adj(T, x, y):
    return [(-2,0),(2,0),(1,1),(-1,1),(1,-1),(-1,-1)]


def solve2(lines):
    
    res = 0

    T = {}

    for line in lines:
        line = line.strip()
        # print(line)
        pos = get_tile_pos(line)
        tile = T.get(pos, "w")
        if tile == "w":
            T[pos] = "b"
        else:
            T[pos] = "w"


    for i in range(100):
        # print(i)
        newT = copy.deepcopy(T)
        xs = list(map(lambda k: k[0], T.keys()))
        ys = list(map(lambda k: k[1], T.keys()))
        minx, maxx = min(xs), max(xs)
        miny,maxy= min(ys), max(ys)
        # print(T)

        for xx in range(min(xs)-1, +max(xs)+2):
            for yy in range(min(ys)-1, +max(ys)+2):
                if (xx % 2) != (yy % 2):
                    continue 
                # print((xx,yy))
                cnt = 0
                for dx,dy in [(-2,0),(2,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
                    p = (xx+dx, yy+dy)
                    tile = T.get(p, "w")
                    if tile == "b":
                        cnt +=1
                # print("adj cnt", cnt)
                me = T.get((xx,yy), "w")
                if me == "b" and (cnt == 0 or cnt > 2):
                    newT[(xx,yy)] = "w"
                    # print("flip")
                elif me == "w" and cnt == 2:
                    newT[(xx,yy)] = "b"
                    # print("flip")
        T = newT
        res = 0
        for k,v in T.items():
            if v == "b":
                res += 1
        print(F"Day {i}: {res}")

    res = 0
    for k,v in T.items():
        if v == "b":
            res += 1

    return res


# t0 = "nwwswee"
# print(get_tile_pos(t0))

# t1 = "esew"
# print(get_tile_pos(t1))


print(solve1(lines))  # 287
print(solve2(lines))  # 3636

stop = datetime.now()
print("duration:", stop - start)