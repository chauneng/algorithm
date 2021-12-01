from sys import stdin

N = int(stdin.readline())
dp = [0] * (N+1)
dp[1] = int(stdin.readline())

if N == 1:
    print(dp[1])
    exit(0)

tmp = dp[1]
for i in range(1, N):
    wine = int(stdin.readline())
    dp[i+1] = max(dp[i-2]+tmp+wine, dp[i-1]+wine, dp[i])
    tmp = wine

print(max(dp[-1], dp[-2]))