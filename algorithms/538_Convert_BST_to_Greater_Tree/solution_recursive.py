# https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():
    total = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
           5
         2   13
        Use a global variable to keep track of the sum of values of nodes with greater node value than the current one
        The base case is the bottom right node
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root