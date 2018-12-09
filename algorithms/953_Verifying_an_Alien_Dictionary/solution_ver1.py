class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        char_order = {char:num for num, char in enumerate(' ' + order)}
        def get_char_at(s, loc):
            if loc >= len(s):
                return ' '
            else:
                return s[loc]

        for loc in range(max(map(len, words))):
            if len(words) == 1:
                return True
            char_nums = [char_order[get_char_at(word, loc)] for word in words]
            if char_nums == sorted(char_nums):
                words = [word for word in words if get_char_at(word, loc) == get_char_at(words[0], loc)]
            else:
                return False
        return True
