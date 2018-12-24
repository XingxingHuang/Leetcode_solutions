"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        queue = [(root, 0)]
        levels = dict()
        depth = 0
        while queue:
            node, level = queue.pop(0)
            depth = max(depth, level)
            levels[level] = levels.get(level, []) + [node.val]
            if node.children:
                queue.extend([(child, level + 1) for child in node.children])
        return [levels[level] for level in range(depth + 1)]
        
            
