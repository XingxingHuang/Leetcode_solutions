import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self._wordList = set(wordList)
        word_used = set(beginWord)
        queue = [[beginWord]]
        shortest_paths = []
        while queue:
            current_level_used_words = set()
            num_paths = len(queue)
            for _ in range(num_paths):
                current_path = queue.pop(0)
                for candidate in self._generateNeighbors(current_path[-1]):
                    if candidate == endWord:
                        shortest_paths.append(current_path + [candidate])
                    elif candidate not in word_used:
                        current_level_used_words.add(candidate)
                        queue.append(current_path + [candidate])
            if shortest_paths:
                return shortest_paths
            word_used |= current_level_used_words
        return shortest_paths

    def _generateNeighbors(self, word):
        candidates = []
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                candidate = word[:i] + letter + word[i + 1:]
                if candidate in self._wordList:
                    candidates += [candidate]
        return candidates

    # @staticmethod
    # def _transformable(str_a, str_b):
    #     diffs = list(map(lambda t: t[0] - t[1], zip(map(ord, str_a), map(ord, str_b))))
    #     # print(str_a, str_b, diffs, sum(map(lambda x: x != 0, diffs)) == 1)
    #     return sum(map(lambda x: x != 0, diffs)) == 1


