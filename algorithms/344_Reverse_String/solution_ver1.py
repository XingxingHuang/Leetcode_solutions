# https://leetcode.com/problems/reverse-string/description/
import timeit

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
def run():
    Solution().reverseString("Hello World")

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)
    print(Solution().reverseString("Hello World"))

if __name__ == '__main__':
    main()
