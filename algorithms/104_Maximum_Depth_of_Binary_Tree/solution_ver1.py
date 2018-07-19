# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        curr = [root]
        next_lev = []
        while curr:
            while curr:
                node = curr.pop()
                if node:
                    if node.left:
                        next_lev.append(node.left)
                    if node.right:
                        next_lev.append(node.right)
            curr = next_lev
            depth += 1
            next_lev = []
        return depth