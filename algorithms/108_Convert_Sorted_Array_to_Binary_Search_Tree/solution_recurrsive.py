# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mean = len(nums) // 2
        tree = TreeNode(nums[mean])
        tree.left = self.sortedArrayToBST(nums[:mean])
        tree.right = self.sortedArrayToBST(nums[mean+1:])
        return tree