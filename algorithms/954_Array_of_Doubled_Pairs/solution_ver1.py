class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def pos_order(B):
            value_counts = dict()
            for value in B:
                value_counts[value] = value_counts.get(value, 0) + 1
            unique_values = sorted(value_counts.keys())
            for value in unique_values:
                while value_counts[value] > 0:
                    if value_counts.get(value * 2, 0) <= 0:
                        return False
                    else:
                        value_counts[value] -= 1
                        value_counts[value * 2] -= 1
            return True
        return pos_order([i for i in A if i >= 0]) and pos_order([-1*i for i in A if i < 0])
