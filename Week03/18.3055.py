from sys import stdin
import heapq

R, C = map(int, stdin.readline().split())
m = []

for _ in range(R):
    m.append(list(stdin.readline().rstrip('\n')))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    time = 1
    while queue:

        t, id, row, column = heapq.heappop(queue)
    
        for i in range(4):
            nRow = row + dx[i]
            nColumn = column + dy[i]
            if not id and 0 <= nRow < R and 0 <= nColumn < C and m[nRow][nColumn] == '.':
                m[nRow][nColumn] = '*'
                heapq.heappush(queue, (time, 0, nRow, nColumn))
    
            if id and 0 <= nRow < R and 0 <= nColumn <C:
                if m[nRow][nColumn] == 'D':
                    return time
                elif id and 0 <= nRow < R and 0 <= nColumn < C and m[nRow][nColumn] == '.':
                    m[nRow][nColumn] = 'S'
                    heapq.heappush(queue, (time, 1, nRow, nColumn))
        time += 1
    return 'KAKTUS'

queue = []

for i in range(R):
    for j in range(C):
        if m[i][j] == '*':
            m[i][j] = 0
            queue.append((0, 0, i, j))
        elif m[i][j] == 'S':
            m[i][j] = 0
            queue.append((0, 1, i, j))

print(bfs())