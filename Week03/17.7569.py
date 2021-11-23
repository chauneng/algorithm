from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())

box = [[] for _ in range(H)]

for i in range(H):
    for _ in range(N):
        box[i].append(list(map(int, stdin.readline().split())))

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
queue = deque()

for i in range(H):
    for j in range(N):
        for l in range(M):
            if box[i][j][l] == 1:
                queue.append((i, j, l))

def bfs():

    while queue:
        level, row, column, = queue.popleft() 

        for l in range(6):
            newLevel = level +dz[l]
            newRow = row + dx[l]
            newColumn = column + dy[l]
            if 0 <= newRow < N and 0 <= newColumn < M and 0 <= newLevel < H and box[newLevel][newRow][newColumn] == 0:
                box[newLevel][newRow][newColumn] = box[level][row][column] + 1
                queue.append((newLevel, newRow, newColumn))

bfs()

def answer():
    ans = -1
    for i in box:
        for j in i:
            for k in j:
                if k == 0:
                    return -1
                ans = max(k, ans)

    return ans-1


print(answer())