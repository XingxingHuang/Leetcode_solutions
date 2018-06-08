# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# class TreeNode:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        stack = [(t1, t2)]
        while stack:
            node1, node2 = stack.pop()
            if not (node1 or node2):
                continue
            node1[val] += node2[val]

            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))

            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
        return t1


