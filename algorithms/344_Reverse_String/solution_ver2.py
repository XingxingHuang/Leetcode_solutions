# https://leetcode.com/problems/reverse-string/description/
import timeit

# recursive solution
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l // 2:]) + self.reverseString(s[:l // 2])

def run():
    Solution().reverseString("Hello World")

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)
    print(Solution().reverseString("Hello World"))

if __name__ == '__main__':
    main()
