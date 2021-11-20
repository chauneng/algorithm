from collections import deque
from sys import stdin

N, M, V = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]

for __ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for ___ in range(1, N+1):
    graph[___].sort()
    
visited = [False] * (N + 1)

def DFS(start: int):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if visited[i] != True:
            DFS(i)

def BFS(start: int):
    visited = [False] * (N + 1)
    print(start, end=' ')
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        for i in graph[queue.popleft()]:
            # print(i)
            if visited[i] != True:
                queue.append(i)
                print(i, end=' ')
                visited[i] = True
    print()

DFS(V)
print()
BFS(V)