from sys import stdin
from collections import deque

N = int(stdin.readline())
altitude = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
def bfs(startRow: int, startColumn: int):
    queue = deque([[startRow, startColumn]])

    while queue:
        row, column = queue.popleft()
        if not visited[row][column]:
            visited[row][column] = cnt
            for i in range(4):
                newRow = row + dx[i]
                newColumn = column + dy[i]
                if 0 <= newRow < N and 0 <= newColumn < N and not visited[newRow][newColumn] and altitude[newRow][newColumn] > rainfall:
                    queue.append([newRow, newColumn])

safearea = 0
for rainfall in range(100):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for row in range(N):
        for column in range(N):
            if altitude[row][column] > rainfall and not visited[row][column]:
                cnt += 1
                bfs(row, column)
    safearea = max(safearea, cnt)

print(safearea)