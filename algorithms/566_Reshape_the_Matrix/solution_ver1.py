# https://leetcode.com/problems/reshape-the-matrix/description/
import timeit

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # sum(nums, []) is iteratively add item from nums(iterable) to []
        values = sum(nums, [])  # = [element for row in nums for element in row]
        if len(values) != r * c:
            return nums
        else:
            return [values[row*c: (row+1)*c] for row in range(r)]

def run():
    Solution().matrixReshape([[1,2], [3,4]], 1, 4)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()