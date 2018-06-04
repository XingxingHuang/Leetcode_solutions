# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _isMirror(self, node1, node2):
        if not (node1 or node2):
            return True
        if not (node1 and node2):
            return False
        return all([node1.val == node2.val, self._isMirror(node1.right, node2.left), self._isMirror(node2.right, node1.left)])

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isMirror(root, root)
