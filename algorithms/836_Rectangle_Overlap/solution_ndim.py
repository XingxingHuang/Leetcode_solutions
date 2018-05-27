# https://leetcode.com/problems/rectangle-overlap/description/


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        ndim = len(rec1) / 2
        return all(max(rec1[i], rec2[i]) < min(rec1[i + ndim], rec2[i + ndim]) for i in range(ndim))
