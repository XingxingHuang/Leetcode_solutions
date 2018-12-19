# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec(node, from_left=False):
            if not node:
                return 0
            if not (node.left or node.right) and from_left:
                return node.val
            return rec(node.left, True) + rec(node.right, False)
        return rec(root)
