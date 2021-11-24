from sys import stdin
from collections import deque

N = int(stdin.readline())
M = int(stdin.readline())

outdegree = {}
parts = {}
needs = {}
queue = deque()

for i in range(1, N+1):
    outdegree[i] = 0
    parts[i] = []
    needs[i] = 0

for _ in range(M):
    a, b, w = map(int, stdin.readline().split())
    parts[a].append((b, w))
    outdegree[b] += 1

for i in range(1, N+1):
    if not outdegree[i]:
        queue.append(i)

while queue:
    p = queue.popleft()
    
    for part in parts[p]:
        num, quantity = part
        needs[num] += quantity
        outdegree[num] -= 1
        needs[p] -= 1
        for i in range(quantity):
            queue.append(num)

for i in range(1, N+1):
    if needs[i]>0:
        print(i, needs[i])