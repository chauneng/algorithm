#Array, dfs, bfs

from collections import deque
# from typing import List

arr = [4,2,3,0,3,1,2]
start = 5

# class Solution:
def canReach(arr, start):
    if start < 0 or start >= len(arr) or arr[start] < 0: return False
    arr[start] *= -1
    return arr[start] == 0 or canReach(arr, start + arr[start]) or canReach(arr, start - arr[start])

print(canReach(arr, start))