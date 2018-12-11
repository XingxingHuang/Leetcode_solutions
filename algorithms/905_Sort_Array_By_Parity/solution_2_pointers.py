class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        front, end = 0, len(A) - 1
        while front < end:
            if A[front] % 2 == 1:
                A[front], A[end] = A[end], A[front]
                end -= 1
            else:
                front += 1
        return A
