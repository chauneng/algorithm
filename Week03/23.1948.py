from sys import stdin
from collections import deque

N = int(stdin.readline())
M = int(stdin.readline())

# adj = {}
# bAdj = {}
# for i in range(1, N+1):
#     adj[i] = set()
#     bAdj[i] = set()

adj = [[]*(N+1) for _ in range(N+1)]
bAdj = [[]*(N+1) for _ in range(N+1)]
outdegree = [0]*(N+1)
indegree = [0]*(N+1)

for _ in range(M):
    a, b, w = map(int, stdin.readline().split())
    adj[a].append([b, w])
    bAdj[b].append([a, w])
    outdegree[a] += 1
    indegree[b] += 1

start, end = map(int, stdin.readline().split())
# print(adj, bAdj)

queue = deque()
queue.append(start)

totalWeight = [0] * (N+1)
while queue:
    crrCity = queue.popleft()
    # print(adj[crrCity])
    for nextCity, weight in adj[crrCity]:
        # print(city, weight)
        indegree[nextCity] -= 1
        totalWeight[nextCity] = max(totalWeight[nextCity], totalWeight[crrCity] + weight)
        if not indegree[nextCity]:
            queue.append(nextCity)

print(totalWeight)