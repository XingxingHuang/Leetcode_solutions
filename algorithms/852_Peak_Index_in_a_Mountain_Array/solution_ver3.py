class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        # binary search
        logN
        """
        low, high = 0, len(A)
        while low < high:
            mid = (low + high) // 2
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low