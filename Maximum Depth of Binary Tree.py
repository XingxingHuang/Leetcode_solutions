# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            lmax = 0
            rmax = 0
            if root.left!=None: lmax =self.maxDepth(root.left)
            if root.right!=None: rmax=self.maxDepth(root.right)
            return max(lmax, rmax)+1
        