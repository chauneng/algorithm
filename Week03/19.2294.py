from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())
coins = sorted(set([int(stdin.readline()) for _ in range(N)]))

queue = deque()

for coin in coins:
    queue.append((1, coin))

def bfs():

    while queue:
        qc, vc = queue.popleft()
        if vc == K:
            return qc
        elif vc < K:
            for coin in coins:
                queue.append((qc+1, vc+coin))

ans = bfs()

if ans is not None:
    print(ans)
else:
    print(-1)