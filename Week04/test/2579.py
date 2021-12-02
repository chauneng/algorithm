from sys import stdin

N = int(stdin.readline())

arr = [int(stdin.readline()) for _ in range(N)]
dp = [0]*N

def solve():
    if not N:
        return 0
    dp[0] = arr[0]
    if N==1:
        return dp[0]
    dp[1] = arr[0]+arr[1]

    for i in range(2, N):
        dp[i] = arr[i] + max(dp[i-2], dp[i-3]+arr[i-1])
    return dp[-1]
    
print(solve())