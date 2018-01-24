class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        B = [abs(x-target) for x in A]
        m = min(B)
        i = B.index(m)
        if m == 0:
            return i
        elif A[i]-target >0:
            return i
        else:
            return i+1
        


'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target not in A:
            A.append(target)
            A.sort()
        return A.index(target)
'''
