from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)

M, N = map(int, stdin.readline().split())
altitude = [list(map(int, stdin.readline().split())) for _ in range(M)]

visited = [[0]*N for _ in range(M)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited[0][0] = 1
ans = 0

dp = set()
def dfs(crrRow: int, crrCol: int, crrAlt: int):
    global ans
    visited[crrRow][crrCol]=1
    for i in range(4):
        newRow = crrRow + dx[i]
        newCol = crrCol + dy[i]
        print(newRow, newCol)
        if 0 <= newRow < M and 0 <= newCol < N and not visited[newRow][newCol]:
            if (newRow, newCol) in dp:
                dp.add((crrRow, crrCol))
                print(dp)
                ans+=1
                continue
            newAlt = altitude[newRow][newCol]
            if newAlt<crrAlt:
                if newRow == M-1 and newCol == N-1 or (newRow, newCol) in dp:
                    dp.add((newRow, newCol))
                    print(dp)
                    ans+=1
                    continue
                dfs(newRow, newCol, newAlt)
            visited[newRow][newCol]=0

dfs(0,0,altitude[0][0])
print(ans)