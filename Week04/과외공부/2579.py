from sys import stdin

NUMBER = int(stdin.readline())
def solve(N):
    if not N:
        return 0
    arr = []
    for _ in range(N):
        arr.append(int(stdin.readline()))
    
    dp = [0]*NUMBER
    dp[0] = arr[0]
    if N==1:
        return dp[0]
    dp[1] = sum(arr[:2])
    if N==2:
        return dp[1]

    for i in range(2, N):
        dp[i] = max(dp[i-2], arr[i-1]+dp[i-3])+arr[i]
    return dp[-1]

print(solve(NUMBER))