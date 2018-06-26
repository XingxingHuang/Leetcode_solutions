# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return None, None
        # root is the smaller branch we concate the smaller sub tree to the right of this root
        elif root.val <= V:
            less_branch, greater_branch = self.splitBST(root.right, V)
            root.right = less_branch
            return root, greater_branch
        # root is the bigger branch we concate the bigger sub tree to the left of this root
        else: # root.val > V
            less_branch, greater_branch = self.splitBST(root.left, V)
            root.left = greater_branch
            return less_branch, root