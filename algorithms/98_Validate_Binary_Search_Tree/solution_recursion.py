# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# buttom up
# The left subtree of a node contains only nodes with keys less than the node's key.
#     ==> the maximum value of left subtree must be less than the node's key
# The right subtree of a node contains only nodes with keys greater than the node's key.
#     ==> the minimum value of right subtree must be greater than the node's key
# Both the left and right subtrees must also be binary search trees.
#     ==> for any subtree in the tree the above two must holds

# top down
# use 


class Solution(object):
    def _isValidBSTNode(self, node, minval, maxval):
        if node is None:
            return True
        if node.val <= minval or node.val >= maxval:
            return False
        return self._isValidBSTNode(node.left, minval, node.val) and self._isValidBSTNode(node.right, node.val, maxval)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBSTNode(root, float('-inf'), float('inf'))