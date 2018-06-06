# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        vocab = {}
        for char in s:
            if char not in vocab:
                vocab[char] = 1
            else:
                vocab[char] += 1
        for char in t:
            if char not in vocab:
                return False
            else:
                vocab[char] -= 1
                if vocab[char] < 0:
                    return False
        return True