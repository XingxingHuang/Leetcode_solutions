# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import namedtuple
Step = namedtuple('step', ['operation', 'node'])

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # using stack
        """
        results, stack = [], []
        stack.append(Step(0, root))
        while stack:
            current = stack.pop()
            if current.node:
                if current.operation == 1:
                    results.append(current.node.val)
                else:
                    stack.extend([Step(0, current.node.right), Step(1, current.node), Step(0, current.node.left)])
        return results
