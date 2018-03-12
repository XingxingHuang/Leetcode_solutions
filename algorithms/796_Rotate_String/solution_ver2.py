# https://leetcode.com/problems/rotate-string/submissions/1


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        same brute force solution, in oneliner
        """
        return B in A + A if len(B) == len(A) else False