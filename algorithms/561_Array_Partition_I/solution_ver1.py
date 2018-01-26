# https://leetcode.com/problems/array-partition-i/description/
import timeit

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([num for i, num in enumerate(nums) if i % 2 == 0])

def run():
    Solution().arrayPairSum([1,4,3,2])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
