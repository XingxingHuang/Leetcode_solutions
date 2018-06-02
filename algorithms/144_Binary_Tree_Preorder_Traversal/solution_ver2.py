# https://leetcode.com/problems/binary-tree-preorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # slightly more concise
        """
        results = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                results.append(node.val)
                stack.extend([node.right, node.left])
        return results
