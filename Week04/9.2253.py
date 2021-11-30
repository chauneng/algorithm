from sys import stdin
from math import sqrt

N, M = map(int, stdin.readline().split())
SMALL = {int(stdin.readline()) for _ in range(M)}

dp = [[float('inf')]*(int(sqrt(2*N))+2) for _ in range(N+1)]
dp[1][0] = 0

for p in range(2, N+1):
    if p in SMALL:
        continue
    for v in range(int(sqrt(2*p)+1)):
        dp[p][v] = min(dp[p-v][v-1], dp[p-v][v], dp[p-v][v+1])+1

ans = min(dp[N])
print(ans) if ans < float('inf') else print(-1)