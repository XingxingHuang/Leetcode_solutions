class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def get_ele_freq(nums):
            freq = dict()
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            return freq

        ele_freq1 = get_ele_freq(nums1)
        ele_freq2 = get_ele_freq(nums2)
        common_ele = set([ele for ele in nums1 if ele in nums2])
        elements = [[ele] * min(ele_freq1[ele], ele_freq2[ele]) for ele in common_ele]
        result = []
        for element in elements:
            result += element
        return result
