# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        curr = [root]
        next_lev = []
        while curr:
            th = []
            while curr:
                node = curr.pop(0)
                th.append(node.val)
                if node.left:
                    next_lev.append(node.left)
                if node.right:
                    next_lev.append(node.right)
            curr = next_lev
            next_lev = []
            ret.append(th)

        return ret  