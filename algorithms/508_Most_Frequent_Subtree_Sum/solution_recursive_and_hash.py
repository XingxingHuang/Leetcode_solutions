# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        sub_tree_sums = []

        def sum_sub_tree(node):
            left_sub_tree_sum = sum_sub_tree(node.left) if node.left else 0
            right_sub_tree_sum = sum_sub_tree(node.right) if node.right else 0
            sub_tree_sum = node.val + left_sub_tree_sum + right_sub_tree_sum
            sub_tree_sums.append(sub_tree_sum)
            return sub_tree_sum

        sum_sub_tree(root)

        max_sum_value_count = 1
        max_sum_values = []
        sum_counts = dict()
        for sub_tree_sum in sub_tree_sums:
            if sub_tree_sum in sum_counts:
                sum_counts[sub_tree_sum] += 1
                max_sum_value_count = max(max_sum_value_count, sum_counts[sub_tree_sum])
            else:
                sum_counts[sub_tree_sum] = 1
        for k in sum_counts:
            if sum_counts[k] == max_sum_value_count:
                max_sum_values.append(k)
        return max_sum_values
