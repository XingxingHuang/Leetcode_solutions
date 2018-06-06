# https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, s):
        if len(s) in [0, 1]:
            return s
        return self.reverseString(s[1:]) + s[0]

