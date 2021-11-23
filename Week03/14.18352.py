from collections import deque
from sys import stdin

N, M, K, X = map(int, stdin.readline().split())
route = [[] for _ in range(N+1)] 
visited = [0] * (N+1)
distance = [0] * (N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    route[a].append(b)

def bfs(start, length):
    ans = []
    queue = deque([start])
    visited[start] = 1
    distance[start] = 0

    while queue:
        location = queue.popleft()
        for i in route[location]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                distance[i] = distance[location] + 1
                if distance[i] == length:
                    ans.append(i)
    
    if len(ans)==0:
        print(-1)
    else:
        for i in sorted(ans):
            print(i, end='\n')

bfs(X, K)