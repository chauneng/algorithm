from sys import stdin
from collections import deque

N = int(stdin.readline())
M = int(stdin.readline())

indegree = [0]*(N+1) 
parts = [[0]*(N+1) for _ in range(N+1)]
queue = deque()

for _ in range(M):
    a, b, w = map(int, stdin.readline().split())
    parts[b][a] = w
    indegree[a] += 1

basic_part = []
for i in range(1, N+1):
    if not indegree[i]:
        queue.append(i)
        basic_part.append(i)

for basic in basic_part:
    parts[basic][basic] = 1

while queue:
    p = queue.popleft()
    for i in range(1, N + 1):
        if parts[p][i] > 0 and indegree[i] > 0:
            for basic in basic_part:
                parts[i][basic] += parts[p][basic] * parts[p][i]
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

for basic in basic_part:
    print(basic, parts[N][basic])