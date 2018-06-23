class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for idx in range(len(A) - 1):
            if A[idx] > A[idx + 1]:
                return idx
