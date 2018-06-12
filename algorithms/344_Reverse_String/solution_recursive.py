# https://leetcode.com/problems/reverse-string/description/

# recursive solution
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l // 2:]) + self.reverseString(s[:l // 2])
