# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curr = root
        stack = []
        head = TreeNode(x=-1)
        header = TreeNode(x=-1)
        header.right = head

        while stack or curr:
            # print(stack, curr)
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if head.val == -1:
                    head.val = curr.val
                else:
                    head.right = TreeNode(x=curr.val)
                    head = head.right
                curr = curr.right
        return header.right