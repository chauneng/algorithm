from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, stdin.readline().rstrip('\n'))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs(startRow, startColumn):
    global queue
    queue.append((startRow, startColumn))

    while queue:
        
        row, column = queue.popleft()
        
        for i in range(4):
            newRow = row + dx[i]
            newColumn = column + dy[i]
        
            if newRow < 0 or newColumn < 0 or newRow >= N or newColumn >= M:
                continue
            elif not maze[newRow][newColumn]:
                continue
            elif maze[newRow][newColumn] == 1:
                maze[newRow][newColumn] = maze[row][column] + 1
                queue.append((newRow, newColumn))
    return maze[N-1][M-1]

print(bfs(0, 0))