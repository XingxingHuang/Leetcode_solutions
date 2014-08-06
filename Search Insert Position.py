class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target not in A:
            A.append(target)
            A.sort()
        return A.index(target)
