# https://leetcode.com/problems/self-dividing-numbers/discuss/109445
import timeit

class Solution:

    def _is_self_dividing(self, number):
        return '0' not in str(number) and all(number % int(digit) == 0 for digit in str(number))

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return list(filter(self._is_self_dividing, range(left, right + 1)))

def run():
    Solution().selfDividingNumbers(1, 2014)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
