class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i,j = 0,1
        while i < len(A)-1:
            while j <= len(A)-1:
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
                j += 1
            i += 1
            j = i+1
        return A
