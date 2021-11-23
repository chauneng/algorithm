from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())
m = []

for _ in range(R):
    m.append(list(stdin.readline().rstrip('\n')))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    time = 0

    while hQueue:
        # if len(wQueue) == 0:
        #     return 'KAKTUS'
        wRow, wColumn = wQueue.popleft()
        for i in range(4):
            newWRow = wRow + dx[i]
            newWColumn = wColumn + dy[i]
            if 0 <= newWRow < R and 0 <= newWColumn < C and m[newWRow][newWColumn] == '.':
                m[newWRow][newWColumn] = '*'
                wQueue.append((newWRow, newWColumn))

        hRow, hColumn = hQueue.popleft()
        for i in range(4):
            newHRow = hRow + dx[i]
            newHColumn = hColumn + dy[i]
            if 0 <= newHRow < R and 0 <= newHColumn <C:
                if m[newHRow][newHColumn] == 'D':
                    return time
                elif m[newHRow][newHColumn] == '.':
                    m[hRow][hColumn] = '.'
                    m[newHRow][newHColumn] = 'S'
                    hQueue.append((newHRow, newHColumn))
        time += 1
    return 'KAKTUS'

wQueue, hQueue = deque(), deque()

for i in range(R):
    for j in range(C):
        if m[i][j] == '*':
            wQueue.append((i, j))
        elif m[i][j] == 'S':
            hQueue.append((i, j))

print(bfs())