from sys import stdin
import heapq

N = int(stdin.readline())
maze = []
visited = []

for _ in range(N):
    maze.append(list(map(int, stdin.readline().rstrip('\n'))))
    visited.append([0]*N)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# print(visited)
def dijkstra(end):
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visited[0][0]=1

    while heap:
        
        cnt, row, column  = heapq.heappop(heap)
        if row == end and column == end:
            return cnt
        
        for i in range(4):
            newRow = row + dx[i]
            newColumn = column + dy[i]
        
            if 0 <= newRow <= end and 0 <= newColumn <= end and visited[newRow][newColumn] == 0:
                visited[newRow][newColumn] = 1
                if maze[newRow][newColumn] == 1:
                    heapq.heappush(heap, [cnt, newRow, newColumn])
                else:
                    heapq.heappush(heap, [cnt+1, newRow, newColumn])

print(dijkstra(N-1))