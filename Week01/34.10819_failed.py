from itertools import permutations
from sys import stdin
from typing import MutableSequence

num = int(stdin.readline())
li = map(int, stdin.readline().split())
maximum = 0
total = 0
def f(m: MutableSequence, a: int):
    global maximum
    global total
    if a == 0:
        if total > maximum:
            maximum=total
            total = 0
            return
        else:
            total = 0
            return
    else:
        total += abs(m[a-1]-m[a])
        a -= 1
        f(m, a)

for i in permutations(li, num):
    f(i, num-1)

print(maximum)