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
        
        def rec(node):
            if not node:
                return []
            ret = [node.val]
            for child in node.children:
                ret.extend(rec(child))
            return ret
        
        return rec(root) 
