from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# .\get.ps1 23

start = datetime.now()
lines = open('23.in').readlines()
line = lines[0]


class Node(object):
    def __init__(self, parent, value, prev, next_):
        self.parent = parent
        self.value = value
        self.prev = prev
        self.next = next_

    def append(self, value):
        node = Node(self.parent, value, self, self.next)
        self.parent.D[value] = node
        self.next = node
        node.next.prev = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        del self.parent.D[self.value]


class LinkedList(object):
    def __init__(self):
        self.D = {}

    def append(self, prev, value):
        if prev is None:
            node = Node(self, value, None, None)
            node.next = node
            node.prev = node
            self.D[value] = node
            return node
        else:
            return prev.append(value)

    def get(self, value):
        assert value in self.D
        return self.D[value]

    def to_list(self):
        res = []
        if len(self.D) == 0:
            return res

        first = next(iter(self.D.values()))
        node = first
        while node.next != first:
            res.append(node.value)
            node = node.next
        res.append(node.value)

        return res


def solve(line, part1):
    rounds = 100 if part1 else 10000000

    nums = []
    for x in list(line.strip()):
        nums.append(int(x))

    if not part1:
        # append more values up to million
        highest = max(nums)
        for i in range(highest + 1, 1000000 + 1):
            nums.append(i)

    l = len(nums)

    LL = LinkedList()
    current = LL.append(None, nums[0])
    node = current
    for x in nums[1:]:
        node = node.append(x)

    for r in range(rounds):
        sel = current.value

        # pick next 3
        current = current.next
        picked_values = []
        for _ in range(3):
            picked = current
            picked_values.append(picked.value)
            current = picked.next
            picked.remove()

        # decrease selected to find destination
        dst = sel
        while dst == sel or dst in picked_values:
            dst -= 1
            if dst == 0:
                dst = l

        # append picked values after destination node
        append_to_node = LL.get(dst)
        for v in picked_values:
            append_to_node = append_to_node.append(v)

    nums = LL.to_list()
    assert len(nums) == l
    pos1 = nums.index(1)

    if part1:
        # concat values appearing after 1
        final = nums[pos1 + 1:] + nums[:pos1]
        res = "".join(map(str, final))
    else:
        # multiply 2 values after 1
        a = nums[(pos1 + 1) % l]
        b = nums[(pos1 + 2) % l]
        res = a * b
    return res


print(solve(line, True))  # 26354798
print(solve(line, False))  # 166298218695

stop = datetime.now()
print("duration:", stop - start)