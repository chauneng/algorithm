# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

# Example 1:
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.

# Example 2:
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127

# Constraints:
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = max(res, nums[i] ^ nums[j])
        return res

# time complexity가 O(n^2)이라 시간초과로 실패함.

