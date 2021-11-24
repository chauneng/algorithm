from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())
coins = sorted(set([int(stdin.readline()) for _ in range(N)]))

queue = deque()
visited = [0] * (100001)

for coin in coins:
    queue.append((1, coin))
    visited[coin] = 1

def bfs():
    while queue:
        qc, vc = queue.popleft()
        if vc == K:
            return qc
        for coin in coins:
            if vc+coin <= K and not visited[vc+coin]:
                queue.append((qc+1, vc+coin))
                visited[vc+coin] = 1

ans = bfs()

if ans is not None:
    print(ans)
else:
    print(-1)