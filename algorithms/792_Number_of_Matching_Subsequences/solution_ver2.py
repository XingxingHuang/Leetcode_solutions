# https://leetcode.com/problems/number-of-matching-subsequences/description/

from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int

        use a dictionary to store the characters scanned per word
            current_char : list of words
        one pass over chars of S:
            pop words started with current char
            strip that leading char from those words and put the rest back into dictionary
        the # words remained in dictionary are those not a subsequence of S
        """
        words_scanned = defaultdict(list)
        for word in words:
            words_scanned[word[0]].append(word)

        for char in S:
            affected_words = words_scanned.pop(char, None)
            if affected_words:
                for word in affected_words:
                    if len(word) > 1:
                        words_scanned[word[1]].append(word[1:])
        return len(words) - sum(len(v) for k, v in words_scanned.items())