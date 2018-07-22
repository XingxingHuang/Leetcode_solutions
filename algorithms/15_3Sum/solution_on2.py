class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        sort first
        iterate over nums[:-2], with idx_a and num_a
            if num_a == previous num_a, skip the iteration
            else:
                make two pointers from idx_b = idx_a + 1 and idx_c = n -1.
                test sum of three, if > 0, reduce idx_c
                                   if < 0, increase idx_b
                                   if equal, move idx_b backward and idx_c forward until they point to numbers that are
                                   different from num_b and num_c
        Careful with indices
        """
        nums.sort()
        n = len(nums)
        results = []

        for idx_a, num_a in enumerate(nums[:-2]):
            if num_a == nums[idx_a - 1] and idx_a != 0:
                continue
            idx_b = idx_a + 1
            idx_c = n - 1
            while idx_b < idx_c:

                num_b = nums[idx_b]
                num_c = nums[idx_c]
                if num_a + num_b + num_c == 0:
                    results.append([num_a, num_b, num_c])
                    while True:
                        if idx_b >= idx_c:
                            break
                        if num_b == nums[idx_b + 1]:
                            idx_b += 1
                        else:
                            break
                    while True:
                        if idx_c <= idx_b:
                            break
                        if num_c == nums[idx_c - 1]:
                            idx_c -= 1
                        else:
                            break
                    idx_b += 1
                    idx_c -= 1
                elif num_a + num_b + num_c > 0:
                    idx_c -= 1
                elif num_a + num_b + num_c < 0:
                    idx_b += 1
        return results