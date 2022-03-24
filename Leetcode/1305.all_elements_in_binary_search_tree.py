# 1305. All Elements in Two Binary Search Trees
# Medium
# Given two binary search trees root1 and root2, 
# return a list containing all the integers from both trees sorted in ascending order.

# Example 1:
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# Constraints:
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, list: List) -> List[int]:
            if not root:
                return
            inorder(root.right, list)
            list.append(root.val)
            inorder(root.left, list)
        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)
        
        ret = []
        while list1 or list2:
            if not list2:
                ret.append(list1.pop())
            elif not list1:
                ret.append(list2.pop())
            elif list1[-1] < list2[-1]:
                ret.append(list1.pop())
            else:
                ret.append(list2.pop())
        
        return ret
