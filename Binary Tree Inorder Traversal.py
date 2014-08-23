# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None: return []
        stack = []
        result = []
        current = root
        while stack != [] or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack.pop()
                result.append(parent.val)
                current = parent.right
        return result
