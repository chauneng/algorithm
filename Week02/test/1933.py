from bisect import insort, bisect_left
from sys import stdin

n = int(stdin.readline())
ss = []

for _ in range(n):
    ss.append(tuple(map(int, stdin.readline().split())))

def getSkyline(buildings):
    if not buildings:
        return []
    height = set()
    for building in buildings:
        L, H, R = building
        height.add((L, -H))
        height.add((R, H))
    ret, queue = [], [0]
    before = queue[-1]
    for P, H in sorted(height):
        if H < 0:
            insort(queue, -H)
        else:
            queue.pop(bisect_left(queue, H))
        if queue[-1] != before:
            ret.append([P, queue[-1]])
            before = queue[-1]
    return ret

print(getSkyline(ss))