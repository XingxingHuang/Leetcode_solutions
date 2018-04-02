# https://leetcode.com/problems/expressive-words/description/
from itertools import groupby


def rle(word):
    """
    :param word: the word to process, like 'heeelloo'
    :return: run length encoding [('h','e','l','o'), (1,3,2,2)]
    """
    return list(zip(*[(k, len(list(group))) for k, group in groupby(word)]))

class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        Divide S and word into group of chars, compare them group by group
        """
        S_ks, S_counts = rle(S)
        counts = 0
        for word in words:
            word_ks, word_counts = rle(word)
            if word_ks != S_ks:
                continue
            counts += all(S_count >= max(word_count, 3) or S_count == word_count for S_count, word_count in
                          zip(S_counts, word_counts))
        return counts
