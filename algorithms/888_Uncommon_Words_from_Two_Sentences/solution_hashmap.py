# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = [word for word in A.split()]
        B = [word for word in B.split()]

        word_freqs = dict()
        for word in A:
            if word not in word_freqs:
                word_freqs[word] = (1, 0)
            else:
                word_freqs[word] = (word_freqs[word][0] + 1, word_freqs[word][1])

        for word in B:
            if word not in word_freqs:
                word_freqs[word] = (0, 1)
            else:
                word_freqs[word] = (word_freqs[word][0], word_freqs[word][1] + 1)

        ret = []
        for word in word_freqs:
            if word_freqs[word] == (0, 1) or word_freqs[word] == (1, 0):
                ret.append(word)
        return ret