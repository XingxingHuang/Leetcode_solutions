#  https://leetcode.com/problems/compare-version-numbers/description/

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        # split numbers by '.' and convert each section into integer
        # pad shorter one with 0
        compare digits by digits
        """
        version1_numbers = [int(i) for i in version1.split('.')]
        version2_numbers = [int(i) for i in version2.split('.')]
        max_len = max(len(version1_numbers), len(version2_numbers))
        version1_numbers += [0] * (max_len - len(version1_numbers))
        version2_numbers += [0] * (max_len - len(version2_numbers))
        for i, j in zip(version1_numbers, version2_numbers):
            if i > j:
                return 1
            elif i < j:
                return -1
        return 0