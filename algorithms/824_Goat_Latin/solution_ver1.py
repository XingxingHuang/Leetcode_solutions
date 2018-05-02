# https://leetcode.com/problems/goat-latin/description/


def transform_word(word):
    if word[0].lower() in 'aeiou':
        return word + 'ma'
    else:
        return word[1:] + word[0] + 'ma'


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return " ".join(transform_word(word) + 'a' * (idx + 1)
                        for idx, word in enumerate(S.split()))