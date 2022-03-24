"""
easy
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""
from typing import List
flowerbed = [1,0,0,0,1]
n = 2
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        else:
            prev= 0
            for lane in flowerbed:
                if not prev and not lane:
                    n -= 1
                    prev = 1
                elif prev and lane:
                    n += 1
                    prev = lane
                else:
                    prev = lane
            if n > 0:
                return False
            else:
                return True