"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                # result = [node.val] + result
                result.append(node.val)
                for child in node.children:
                    stack.append(child)
        # return result
        return result[::-1]
