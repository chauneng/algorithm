N, M = 5, 6

maze = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

visited = [[0] * M for _ in range(N)]
res = [float('inf')]

def dfs(row, column, step):
    if row == N-1 and column == M-1:
        res.append(step)
        return
    else:
        if not maze[row][column] or visited[row][column]:
            return
        else:
            visited[row][column] = 1
            if row - 1 >= 0:
                dfs(row-1, column, step+1)
            if row + 1 < N:
                dfs(row+1, column, step+1)
            if column - 1 >= 0:
                dfs(row, column-1, step+1)
            if column + 1 < M:
                dfs(row, column+1, step+1)

dfs(0, 0, 1)
print(min(res))