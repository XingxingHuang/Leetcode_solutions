# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        values = []
        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        if len(values) < 2:
            return

        values.sort()
        diffs = map(lambda x: abs(x[0] - x[1]), zip(values[1:], values[:-1]))
        return min(diffs)
