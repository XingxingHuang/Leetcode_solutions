# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
import timeit

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(["".join([char for char in word][::-1]) for word in s.split()])

def run():
    Solution().reverseWords("Let's take LeetCode contest")

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)
    print(Solution().reverseWords("Let's take LeetCode contest"))

if __name__ == '__main__':
    main()
