import sys
from heapq import heappop, heappush

def topology_sort():
    q = []
    for i in range(1, n + 1):
        if degree[i] == 0:
            heappush(q, -i)
    N = n
    while q:
        now = -heappop(q)
        anw[now] = N

        for k in graph[now]:
            degree[k] -= 1
            if not degree[k]:
                heappush(q, -k)
        N -= 1

n = int(sys.stdin.readline())
anw = [0] * (n + 1)
degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = [0] + list(map(int, sys.stdin.readline().rstrip()))
    for j in range(1, n + 1):
        if tmp[j]:
            graph[j].append(i)
            degree[i] += 1
topology_sort()
if anw.count(0) > 1:
    print(-1)
else:
    print(*anw[1:])