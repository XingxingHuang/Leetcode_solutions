# https://leetcode.com/problems/rotate-string/submissions/1


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        brute force, check every rotation of A
        """
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False