class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len, reverse=True)
        words = [word + '#' for word in words]
        indexes, S = [], ''
        for word in words:
            if word in S:
                indexes.append(S.index(word))
            else:
                indexes.append(len(S))
                S += word
        return len(S)
