class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        l = len(A[0])
        cols_to_delete = []
        for i in range(l):
            chars_at_loc = [s[i] for s in A]
            if chars_at_loc != sorted(chars_at_loc):
                cols_to_delete.append(i)
        return len(cols_to_delete)
