from sys import stdin

N = int(stdin.readline())

dp = [0] * N
dp[0] = int(stdin.readline())

if N == 1:
    print(dp[0])
    exit(0)
elif N == 2:
    dp[1] = int(stdin.readline())
    print(sum(dp))
    exit(0)

tmp = dp[0]
for i in range(N-1):
    wine = int(stdin.readline())
    dp[i+1] = max(dp[i-2]+tmp+wine, dp[i-1]+wine, dp[i])
    tmp = wine

print(max(dp[-1], dp[-2])) 