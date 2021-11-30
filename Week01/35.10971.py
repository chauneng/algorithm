from sys import stdin

N = int(stdin.readline())
fare = [list(map(int, stdin.readline().split())) for _ in range(N)]

def dfs(start: int,departure: int, part_sum: int) -> None:
    global ans

    if part_sum > ans:
        return 

    if sum(visited) == N:
        if fare[departure][start]:
            part_sum += fare[departure][start]
            ans = min(ans, part_sum)
            return 
    
    for arrive in range(N):
        if not visited[arrive]:
            if not fare[departure][arrive]:
                return 
            else:
                visited[arrive] = 1
                dfs(start, arrive, part_sum + fare[departure][arrive])
                visited[arrive] = 0

ans = float('inf')
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0)
    visited[i] = 0

print(ans)