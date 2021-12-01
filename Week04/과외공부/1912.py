from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))



# 음수가 될 때까지 쭉 더하다가?, 음수가 되면 그 점에서 끊고 다시 시작해보기
dp = [-float('inf')]
tmp = 0
for i in range(N):
    if tmp + arr > dp[0]:
        tmp += arr[i]