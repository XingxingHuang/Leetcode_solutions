# https://leetcode.com/problems/range-addition-ii/description/
import timeit


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        return min([op[0] for op in ops]) * min([op[1] for op in ops])


def run():
    Solution().maxCount(3, 3, [[2,2],[3,3]])


def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)


if __name__ == '__main__':
    main()