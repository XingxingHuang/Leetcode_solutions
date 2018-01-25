# https://leetcode.com/problems/self-dividing-numbers/discuss/109445
import timeit

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        results = []
        for number in range(left, right + 1):
            found = True
            if '0' in str(number):
                found = False
            else:
                digits = [i for i in str(number)]
                for digit in digits:
                    if number % int(digit) != 0:
                        found = False
            if found:
                results.append(number)
        return results

def run():
    Solution().selfDividingNumbers(1, 2014)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
