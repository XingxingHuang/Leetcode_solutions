"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        to_visit = [root]
        vals = []
        while to_visit:
            node = to_visit.pop(0)
            if not node:
                continue
            if node.val is not None:
                vals.append(node.val)
            if node.children:
                to_visit = node.children + to_visit
        return vals
