class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        let s = 'abcabc' pattern * 2
        s[1:] + s[:-1] = 'bcabcabcab' which should contain 2 patterns
        so s should in it
        """
        return s in (s[1:] + s[:-1])