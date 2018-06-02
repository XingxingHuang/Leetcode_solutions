# https://leetcode.com/problems/binary-tree-postorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # recursive
        """
        if not root: return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]