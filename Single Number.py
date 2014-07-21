class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for i in range(len(A)):
            try:
                A[i:].remove(A[i])
            except:
                return A[i]