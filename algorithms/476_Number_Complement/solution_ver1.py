# https://leetcode.com/problems/number-complement/description/
import timeit

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 1 << num.bit_length() - 1 is the number with same bit length as num which is 1 everywhere
        # num ^ which is flipping every digit
        return num ^ ((1<<num.bit_length())-1)

def run():
    Solution().findComplement(16)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)
    print(Solution().findComplement(5))

if __name__ == '__main__':
    main()
