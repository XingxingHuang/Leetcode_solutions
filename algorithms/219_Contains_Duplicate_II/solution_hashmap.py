class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_idx_mapping = dict()
        for idx, num in enumerate(nums):
            if num not in num_idx_mapping:
                num_idx_mapping[num] = [idx]
            else:
                num_idx_mapping[num].append(idx)

        for num, matched_idx in num_idx_mapping.items():
            if any(map(lambda x: abs(x[0] - x[1]) <= k, zip(matched_idx[1:], matched_idx[:-1]))):
                # watch out the corner case here
                # if len(matched_idx) == 1, it is zip([], []) which is [],
                # mapping a function to element of [] is not evaluated at all, so it is safe.
                return True
        return False