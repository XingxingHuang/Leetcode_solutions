# https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, s):
        r = ""
        n = len(s)
        for i in range(n):
            r += s[n - i - 1]
        return r

