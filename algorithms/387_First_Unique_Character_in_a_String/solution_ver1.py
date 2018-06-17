from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_loc = defaultdict(list)
        for idx, char in enumerate(s):
            char_loc[char].append(idx)
        return min(sum([val for key, val in char_loc.items() if len(val) == 1], []), default=-1)
