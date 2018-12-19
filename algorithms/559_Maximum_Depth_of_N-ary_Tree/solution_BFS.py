"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        max_depth = 0
        if not root:
            return max_depth
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            max_depth = max(max_depth, level)
            for child in node.children:
                stack.append((child, level + 1))
        return max_depth
