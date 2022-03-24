cast = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

visited = [[0] * 5 for _ in range(4)]
res = 0

def dfs(row, column):
    if (cast[row][column] == 0 and not visited[row][column]):
        visited[row][column] = 1
        if row-1 >= 0:
            dfs(row-1, column)
        if row+1 < 4:
            dfs(row+1, column)
        if column-1 >= 0:
            dfs(row, column-1)
        if column+1 < 5:
            dfs(row, column+1)
        return 1
    else:
        return 0

for i in range(4):
    for j in range(5):
        res += dfs(i, j)

print(res)