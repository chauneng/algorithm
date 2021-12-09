#Array, dfs, bfs

from collections import deque
from typing import List

arr = [4,2,3,0,3,1,2], 
start = 5

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
            if not arr[start]:
                return True
            else:
                queue = deque()
                dx = [1, -1]
                visitied = [0]*len(arr)
                queue.append(start)
                visitied[start] = 1
                while queue:
                    crr_index = queue.popleft()
                    for i in range(2):
                        new_index = crr_index + (dx[i]*arr[crr_index])
                        if 0 <= new_index < len(arr):
                            if visitied[new_index]:
                                continue
                            else:
                                if not (arr[new_index]):
                                    return True
                                else:
                                    visitied[new_index] = 1
                                    queue.append(new_index)
                return False