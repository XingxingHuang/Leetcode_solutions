class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        r = [''] * n
        for idx, char in enumerate(s):
            r[n - idx - 1] = char
        return "".join(r)