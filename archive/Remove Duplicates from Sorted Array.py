class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == []:
            return 0
        else:
            i = 0
            for j in range(1,len(A)):
                if A[i] != A[j]: 
                    i +=1
                    A[i] = A[j]
            return i+1
