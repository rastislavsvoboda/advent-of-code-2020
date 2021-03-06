from datetime import datetime

# .\get.ps1 23

start = datetime.now()
lines = open('23.in').readlines()
line = lines[0]


def solve(line, part1):
    rounds = 100 if part1 else 10_000_000

    ns = list(map(int, list(line.strip())))

    if not part1:
        highest = max(ns)
        for i in range(highest + 1, 1_000_000 + 1):
            ns.append(i)

    l = len(ns)

    # nexts store "pointers"
    # index is the number value itself
    # next[index] is the value of the following item
    # 0 index is not used, 0 is not in the list
    nexts = [None] * (l+1)

    s = ns[0]
    for x in ns[1:]:
        nexts[s] = x
        s = x
    nexts[s] = ns[0]

    selected = ns[0]
    
    for r in range(rounds):    
        p1 = nexts[selected]
        p2 = nexts[p1]
        p3 = nexts[p2]

        dst = selected
        while dst == selected or dst == p1 or dst == p2 or dst == p3:
            dst = dst - 1 if dst > 1 else l

        # previously was:
        #    (selected) -> p1 -> p2 -> p3 -> p3_next ... dst -> dst_next ...
        # now it should be:
        #    selected -> (p3_next) ... dst -> p1 -> p2 -> p3 -> dst_next ...
        # with old p3_next as new selected
        nexts[selected] = nexts[p3]
        nexts[p3] = nexts[dst]
        nexts[dst] = p1
        selected = nexts[selected]

    if part1:
        res = ""
        x = nexts[1]
        while x != 1:
            res += str(x)
            x = nexts[x]
    else:
        a = nexts[1]
        b = nexts[a]
        res = a * b
    return res


print(solve(line, True))  # 26354798
print(solve(line, False))  # 166298218695

stop = datetime.now()
print("duration:", stop - start)