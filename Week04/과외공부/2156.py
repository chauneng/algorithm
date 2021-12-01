from sys import stdin

N = int(stdin.readline())

dp = [0] * N

if N == 1:
    print(stdin.readline())
else:
    for i in range(N):
       dp[i] = int(stdin.readline())

    if N < 3:
        print(sum(dp))
        exit(0)

    wine = int(stdin.readline())

    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3, N):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

    print(max(dp[-1], dp[-2]))