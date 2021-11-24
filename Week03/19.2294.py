from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())
coin = sorted(set([int(stdin.readline()) for _ in range(N)]))

# coin = sorted(set(coin))
v = 0
q = 0

def bfs():
    global q
    global v
    queue = deque()

    for i in coin:    
        queue.append(q+1, v+i)
    q += 1

    while queue:

        nc, vc = queue.popleft()
        if vc == K:
            print(nc)
        else:
