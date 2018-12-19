# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def _dfs(node, result=[]):
            if not node:
                result += []
            elif not (node.left or node.right):
                result += [node.val]
            else:
                result = _dfs(node.left, result)
                result = _dfs(node.right, result)
            return result
        return _dfs(root1, []) == _dfs(root2, [])
