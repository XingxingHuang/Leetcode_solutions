class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not wordList:
            return 0
        self._paths = []
        self._end_word = endWord
        self._find_path([beginWord], beginWord, set(wordList))
        # print(self._paths)
        return min(map(len, self._paths)) if self._paths else 0

    def _transformable(self, str_a, str_b):
        diffs = list(map(lambda t: t[0] - t[1], zip(map(ord, str_a), map(ord, str_b))))
        # print(str_a, str_b, diffs, sum(map(lambda x: x != 0, diffs)) == 1)
        return sum(map(lambda x: x != 0, diffs)) == 1

    '''
    # should be slightly faster helper but still tle
    @staticmethod
    def _transformable(str_a, str_b):
        num_diff = 0
        for char_a, char_b in zip(str_a, str_b):
            if num_diff > 1:
                return False
            if char_a != char_b:
                num_diff += 1
        return num_diff == 1
    '''

    def _find_path(self, current_path, current_word, remaining_words):
        if current_word == self._end_word:
            self._paths.append(current_path)
            return
        if self._transformable(current_word, self._end_word):
            self._find_path(current_path + [self._end_word], self._end_word, {})
        else:
            for next_word in remaining_words:
                if self._transformable(current_word, next_word):
                    # print(current_word, next_word)
                    self._find_path(current_path + [next_word], next_word, remaining_words - {next_word})


