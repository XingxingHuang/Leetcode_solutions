# https://leetcode.com/problems/toeplitz-matrix/description/
import timeit

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[row_index + 1][1:] == matrix[row_index][:-1] for row_index in range(len(matrix)-1))

def run():
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Solution().isToeplitzMatrix(matrix)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
