
nums = [-2, 2]

dp = [[0,0] for _ in range(len(nums))]
dp[0][0] = dp[0][1] = nums[0] 
if len(nums)>1:
    for i in range(1, len(nums)):
        dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        ans = 0
        for i in range(len(nums)):
            ans = max(dp[i][0], ans)
            ans = max(dp[i][1], ans)
        print(ans)
else:
    print(nums[0])
# print(dp)