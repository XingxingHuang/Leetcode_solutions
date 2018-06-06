# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        lets say p.val < q.val
        lowest common ancestor is the node with value p.val <= node.val <= q.val
        we can traversal the tree from root, trying to find the first node that satisfy this condition
        """
        if root is None:
            return None
        if q.val < root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if q.val > root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root