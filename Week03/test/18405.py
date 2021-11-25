# 60%쯤에서 틀렸습니다가 나오네 ㅠ

from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

arr = []
timetable = [[int(1e9)]*N for _ in range(N)]
virus = [[0]*N for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, stdin.readline().split())))

S, X, Y = map(int, stdin.readline().split())

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            timetable[i][j] = 0

def spread(virusType):
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == virusType:
                queue.append((i, j))
                timetable[i][j] = 0
                virus[i][j] = virusType
    
    while queue:
        
        row, column = queue.popleft()

        for i in range(4):
            newRow = row + dx[i]
            newColumn = column + dy[i]
            
            if 0 <= newRow < N and 0 <= newColumn < N and timetable[row][column] + 1 < timetable[newRow][newColumn]:
                timetable[newRow][newColumn] = timetable[row][column] + 1
                virus[newRow][newColumn] = virusType
                if timetable[newRow][newColumn] < S:
                    queue.append((newRow, newColumn))

for i in range(1, K+1):
    spread(i)

print(virus[X-1][Y-1])