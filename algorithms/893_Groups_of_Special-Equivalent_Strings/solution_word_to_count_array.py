class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def _word_to_char_counts(word):
            c = [0] * 52
            for idx, char in enumerate(word):
                loc = 0 if idx % 2 == 0 else 26
                loc += ord(char) - ord('a')
                c[loc] += 1
            return tuple(c)
        return len(set(_word_to_char_counts(word) for word in A))

