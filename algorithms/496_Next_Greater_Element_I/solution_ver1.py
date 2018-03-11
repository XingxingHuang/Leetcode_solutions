# https://leetcode.com/problems/next-greater-element-i/description/


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = []
        for num1 in nums1:
            for num2 in nums2[nums2.index(num1):]:
                if num2 > num1:
                    results.append(num2)
                    break
            else:
                results.append(-1)
        return results