class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_counts = dict()
        for char in magazine:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        for char in ransomNote:
            if char not in char_counts:
                return False
            else:
                char_counts[char] -= 1
                if char_counts[char] == 0:
                    del char_counts[char]
        return True