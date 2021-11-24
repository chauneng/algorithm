from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())
m = []
visited = []

for _ in range(R):
    m.append(list(stdin.readline().rstrip('\n')))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wQueue, hQueue = deque(), deque()

for i in range(R):
    for j in range(C):
        if m[i][j] == '*':
            # m[i][j] = 0
            wQueue.append((i, j))
        elif m[i][j] == 'S':
            # m[i][j] = 0
            hQueue.append((i, j, 0))

while wQueue:
    # if len(wQueue) == 0:
    #     return 'KAKTUS'
    wRow, wColumn = wQueue.popleft()
    for i in range(4):
        newWRow = wRow + dx[i]
        newWColumn = wColumn + dy[i]
        if 0 <= newWRow < R and 0 <= newWColumn < C and m[newWRow][newWColumn] == '.':
            m[newWRow][newWColumn] = m[wRow][wColumn] + 1
            wQueue.append((newWRow, newWColumn))

while hQueue:
    hRow, hColumn, day = hQueue.popleft()
    if m[hRow][hColumn] == 'D':
        day += 1
        break
    for i in range(4):
        newHRow = hRow + dx[i]
        newHColumn = hColumn + dy[i]
        if 0 <= newHRow < R and 0 <= newHColumn <C and not visited[newHRow][newHColumn]:
            if m[newHRow][newHColumn] == '.' and m[newHRow][newHColumn] > day+1 :
                hQueue.append((newHRow, newHColumn, day+1))

if goal:
    print(day)
else:
    print('KAKTUS')