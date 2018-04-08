#  https://leetcode.com/problems/binary-tree-pruning/description/
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

TAGS = ['TREE', 'RECURSION']

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        recursive solution
        """
        if not root:
            return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if not left:
            root.left = None
        if not right:
            root.right = None

        return root if (root.val == 1 or left or right) else None
