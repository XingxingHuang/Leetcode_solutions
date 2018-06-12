# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = dict()
        for char in s:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1

        for idx, char in enumerate(s):
            if char_counts[char] == 1:
                return idx
        return -1
