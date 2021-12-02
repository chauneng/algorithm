from sys import stdin

N = int(stdin.readline())

dp, arr = [], []
for _ in range(N+1):
    dp.append([0, 0, 0])
    arr.append([0, 0, 0])

for i in range(1, N+1):
    f, s, t = map(int, stdin.readline().split())
    arr[i][0], arr[i][1], arr[i][2] = f, s, t

for i in range(1, N+1):
    for j in range(3):
        dp[i][j] = arr[i][j]+min(dp[i-1][j-1], dp[i-1][j-2])

print(min(dp[N]))