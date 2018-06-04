# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.extend([root, root])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not (node1 or node2):
                continue
            if not (node1 and node2):
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node2.right)
            queue.append(node1.left)
        return True
