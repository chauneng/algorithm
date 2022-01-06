class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root):
        if not root:
            return []
        ret, level = [], [root]
        while level:
            nextlevel, value = [], []
            for node in level:
                value.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            ret.append(value)
            level = nextlevel
        return ret
        