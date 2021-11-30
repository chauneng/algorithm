from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
SMALL = {int(stdin.readline()) for _ in range(M)}

dx = (-1, 0, 1)

queue = deque()
queue.append([1, 1, 0])
ans = -1
while queue:
    speed, position, jump = queue.popleft()
    if N == speed+position:
        ans = jump
        break

    for i in range(3):
        newSpeed = speed+dx[i]
        if newSpeed>0 and (newSpeed+position) not in SMALL:
            queue.append([newSpeed, position+speed, jump+1])

print(ans)