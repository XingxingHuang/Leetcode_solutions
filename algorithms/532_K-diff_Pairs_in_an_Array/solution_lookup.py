class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        if k == 0, the any duplicated number counts
        if k > 0, check i + k in number or not, this is sufficient, do not need to check i - k as it will count duplicate
            since (i, j) and (j, i) with |i - j| == k only counts once
        """
        num_counts = dict()
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1

        total_pairs = 0
        for num in num_counts:
            if (k == 0 and num_counts[num] > 1) or (k > 0 and num + k in num_counts):
                total_pairs += 1
        return total_pairs
