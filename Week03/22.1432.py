from sys import stdin
from collections import deque

N = int(stdin.readline())
adj = [[0]*(N+1)]

for _ in range(N):
    a = list(map(int, stdin.readline().rstrip('\n')))
    a.insert(0,0)
    adj.append(a)

queue = deque()
outdegree = [0] * (N+1)

graph = {}
for i in range(1, N+1):
    graph[i] = set()
for i in range(1, N+1):
    for j in range(1, N+1):
        if adj[i][j]:
            graph[j].add(i)
            outdegree[i] += 1
# print(graph)
# print(outdegree)
flag = False
for i in range(1, N+1):
    if not outdegree[i]:
        queue.append(i)
        flag = True
# print(queue)

vertex = {}
for i in range(1, N+1):
    vertex[i] = i

while queue:
    crrV = queue.popleft()
    for adjV in graph[crrV]:
        
        if vertex[adjV] > vertex[crrV]:
            vertex[adjV] = vertex[crrV]
            vertex[crrV] = adjV
            queue.append(adjV)

if flag:
    for i in range(1, N):
        print(vertex[i], end=' ')
    print(vertex[N])
else:
    print(-1)