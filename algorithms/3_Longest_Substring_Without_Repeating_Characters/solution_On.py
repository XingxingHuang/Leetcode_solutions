# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        # use a sliding window, keep track of set of unique chars in window
        # expand to the right when possible
        # when encountering duplicate on right hand side, shrink window from left to remain unique
        # update max when window expands
        """
        n = len(s)
        chars = set()
        l = 0
        start = 0
        end = 0
        while start < n and end < n:
            if s[end] not in chars:
                chars.add(s[end])
                end += 1
                l = max(l, end - start)
            else:
                chars.remove(s[start])
                start += 1
        return l
