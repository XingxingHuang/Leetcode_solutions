# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    # brute force solution, scan the longest non repeated substring starting from each possible starting location
    # O(n^2)
    def lengthOfLongestSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        return max([self.__longest_non_repeated_prefix(s[i:]) for i in range(len(s))], default = 0)

    @staticmethod
    def __longest_non_repeated_prefix(s):
        charset = {}
        for char in s:
            if char not in charset:
                charset[char] = 1
            else:
                return len(charset)
        return len(s)