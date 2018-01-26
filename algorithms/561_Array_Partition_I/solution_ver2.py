# https://leetcode.com/problems/array-partition-i/description/
import timeit

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

def run():
    Solution().arrayPairSum([1,4,3,2])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
