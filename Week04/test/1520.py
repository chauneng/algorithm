from sys import stdin
from sys import setrecursionlimit
# from collections import deque
setrecursionlimit(10**6)

M, N = map(int, stdin.readline().split())
altitude = [list(map(int, stdin.readline().split())) for _ in range(M)]

visited = [[0]*N for _ in range(M)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
# queue = deque()
# queue.append((0, 0, altitude[0][0]))
visited[0][0] = 1
# possible = set()
ans = 0
# def bfs():
#     global ans
#     while queue:
#         crrRow, crrCol, crrAlt = queue.popleft()
#         visited[crrRow][crrCol] = 1

#         if crrRow==M-1 and crrCol==N-1 or (crrRow, crrCol, crrAlt) in possible:
#             print(crrRow,crrCol)
#             ans += 1
#             possible.add((crrRow, crrCol, crrAlt))
#             continue

#         for i in range(4):
#             newRow = crrRow + dx[i]
#             newCol = crrCol + dy[i]
            
#             if 0 <= newRow < M and 0 <= newCol < N and not visited[newRow][newCol]:
#                 newAlt = altitude[newRow][newCol]
#                 if newAlt<crrAlt:
#                     if (newRow, newCol, newAlt) in possible:
#                         possible.add((crrRow, crrCol, crrAlt))
#                         continue
#                     queue.append((newRow, newCol, newAlt))

# bfs()
# print(ans)

dp = set()
def dfs(crrRow: int, crrCol: int, crrAlt: int):
    global ans
    visited[crrRow][crrCol]=1
    for i in range(4):
        newRow = crrRow + dx[i]
        newCol = crrCol + dy[i]
        if 0 <= newRow < M and 0 <= newCol < N and not visited[newRow][newCol]:
            if (newRow, newCol) in dp:
                dp.add((crrRow,crrCol))
                print(dp)
                ans+=1
                continue
            newAlt = altitude[newRow][newCol]
            if newAlt<crrAlt:
                if newRow == M-1 and newCol == N-1 or (newRow, newCol) in dp:
                    dp.add((newRow,newCol))
                    print(dp)
                    ans+=1
                    continue
                dfs(newRow, newCol, newAlt)
            visited[newRow][newCol]=0

dfs(0,0,altitude[0][0])
print(ans)