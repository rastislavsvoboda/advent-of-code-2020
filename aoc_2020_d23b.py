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


def solve1(line):
    nums = []
    for x in list(line.strip()):
        nums.append(int(x))

    l = len(nums)        

    LL = LinkedList()
    current = LL.append(None, nums[0])
    node = current
    for x in nums[1:]:
        node = node.append(x)

    for r in range(100):
        sel = current.value
        p1 = current.next
        p2 = p1.next
        p3 = p2.next
        current = p3.next

        p1.remove()
        p2.remove()
        p3.remove()

        p1_val = p1.value
        p2_val = p2.value
        p3_val = p3.value

        dst = sel
        while dst == sel or dst == p1_val or dst == p2_val or dst == p3_val:
            dst -= 1
            if dst == 0:
                dst = l

        dst_node = LL.get(dst)
        p1_ = dst_node.append(p1_val)
        p2_ = p1_.append(p2_val)
        p3_ = p2_.append(p3_val)

    nums = LL.to_list()
    pos1 = nums.index(1)
    final = nums[pos1 + 1:] + nums[:pos1]
    res = "".join(map(str, final))
    return res


def solve2(line):
    nums = []
    for x in list(line.strip()):
        nums.append(int(x))

    highest = max(nums)
    for i in range(highest + 1, 1000000 + 1):
        nums.append(i)
 
    l = len(nums)       

    LL = LinkedList()
    current = LL.append(None, nums[0])
    node = current
    for x in nums[1:]:
        node = node.append(x)

    for r in range(10000000):
        sel = current.value
        p1 = current.next
        p2 = p1.next
        p3 = p2.next
        current = p3.next

        p1.remove()
        p2.remove()
        p3.remove()

        p1_val = p1.value
        p2_val = p2.value
        p3_val = p3.value

        dst = sel
        while dst == sel or dst == p1_val or dst == p2_val or dst == p3_val:
            dst -= 1
            if dst == 0:
                dst = l

        dst_node = LL.get(dst)
        p1_ = dst_node.append(p1_val)
        p2_ = p1_.append(p2_val)
        p3_ = p2_.append(p3_val)

    nums = LL.to_list()
    assert len(nums) == l
    pos1 = nums.index(1)
    a = nums[(pos1 + 1) % l]
    b = nums[(pos1 + 2) % l]
    res = a * b
    return res


print(solve1(line))  # 26354798
print(solve2(line))  # 166298218695

stop = datetime.now()
print("duration:", stop - start)