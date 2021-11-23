from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())

box = [[] for _ in range(H)]
visited = [[] for _ in range(H)]

for i in range(H):
    for _ in range(N):
        box[i].append(list(map(int, stdin.readline().split())))
        visited[i].append([0]*M)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# print(visited)

def bfs():

    queue = deque()
    queue.appendleft((0, 0, 0))

    row, column, level = queue.popleft()
    

    days = 0
    
    while queue:
         
        for i in box:
            for j in i:
                for k in j:
                    if k == 1:
                        visited[i][j][k] = 1
                        for l in range(6):
                            newRow = row + dx[l]
                            newColumn = column +dy[l]
                            newLevel = level +dz[l]
                            if 0 <= newRow <= N-1 and 0 <= newColumn <= M-1 and 0 <= newLevel<= H-1 and visited[newRow][newColumn][newLevel] == 0:
                                queue.append((i, j, k))

bfs()
print(visited)