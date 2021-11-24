from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())

graph = [[] for _ in range(N+1)]
result = []
indgree = {}
queue = deque()

for i in range(1, N+1):
    indgree[i] = 0

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    indgree[b] += 1

for i in range(1, N+1):
    if not indgree[i]:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)

    for i in graph[now]:
        indgree[i] -= 1
        if not indgree[i]:
            queue.append(i)

print(*result)