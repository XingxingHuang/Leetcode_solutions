# https://leetcode.com/problems/hamming-distance/description/
import timeit

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")

def run():
    x = 1
    y = 4
    Solution().hammingDistance(x, y)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
