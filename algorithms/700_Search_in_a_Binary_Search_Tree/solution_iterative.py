# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if node.left and val < node.val:
                stack.append(node.left)
            if node.right and val > node.val:
                stack.append(node.right)
        return None
