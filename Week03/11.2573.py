import sys
from collections import deque
sys.setrecursionlimit(10**5)


N, M = map(int, sys.stdin.readline().split())
coordinate = {}
queue = deque()
ans = 0
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    coordinate[i] = list(map(int, sys.stdin.readline().split()))

def dfs(row: int, column: int):
    visited[row][column] = True

    for i in range(4):
        nx = row + dx[i]
        ny = column + dy[i]

        if not visited[nx][ny] and coordinate[nx][ny]:
            dfs(nx, ny)

def nThow(row, column):
    degree = 0
    for i in range(4):
        nx = row + dx[i]
        ny = column + dy[i]
        if not coordinate[nx][ny]:
            degree -= 1
    if degree:
        return (row, column, degree)


while True:

    ans += 1

    for i in range(1, N):
        for j in range(1, M):
            if coordinate[i][j]:
                queue.append(nThow(i, j))
    
    while queue:
        thaw = queue.popleft()
    if thaw != None:
        coordinate[thaw[0]][thaw[1]] = max(coordinate[thaw[0]][thaw[1]] + thaw[2], 0)

    visited =[[0] * (M) for _ in range(N)]

    for i in range(1, N):
        for j in range(1, M):
            if coordinate[i][j] and not visited[i][j]:
                    cnt += 1
                    if cnt == 2:
                        break
                    dfs(i, j)
    
    if cnt > 1:
        break
    
    melt = 0
    for i in range(N):
        for j in range(M):
            melt += coordinate[i][j]
    if not melt:
        ans = 0
        break

print(ans)
