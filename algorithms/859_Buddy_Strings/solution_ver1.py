class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) < 2 or len(B) < 2 or len(A) != len(B):
            return False
        if A == B:
            return len(A) > len(set(A))
        sA = ''
        sB = ''
        for i, char in enumerate(A):
            if char != B[i]:
                sA += char
                sB += B[i]
        if len(sA) == 2:
            return sA[::-1] == sB
        return False
