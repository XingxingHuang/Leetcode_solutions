# https://leetcode.com/problems/keyboard-row/description/
import timeit

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word
                for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
                    for word in words
                        if set(word.lower()) <= row
                ]

def run():
    Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))

if __name__ == '__main__':
    main()
