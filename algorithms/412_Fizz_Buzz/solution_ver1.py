# https://leetcode.com/problems/fizz-buzz/description/
import timeit

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [self._parse_number(i) for i in range(1, n+1)]

    def _parse_number(self, i):
        results = ""
        if i % 3 == 0:
            results += "Fizz"
        if i % 5 == 0:
            results += "Buzz"
        if (i % 3 != 0) and (i % 5 != 0):
            results += str(i)
        return results


def run():
    Solution().fizzBuzz(15)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
