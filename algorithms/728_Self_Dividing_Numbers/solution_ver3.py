# https://leetcode.com/problems/self-dividing-numbers/discuss/109445
import timeit
from multiprocessing import Pool

class Solution:

    def _is_self_dividing(self, number):
        if '0' not in str(number) and all(number % int(digit) == 0 for digit in str(number)):
            return number
        else:
            return None

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        pool = Pool(8)
        results = [i for i in pool.map(self._is_self_dividing, range(1, 1024)) if i is not None]
        pool.close()
        return results

def run():
    Solution().selfDividingNumbers(1, 2014)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
