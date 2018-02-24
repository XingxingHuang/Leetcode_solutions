# https://leetcode.com/problems/spiral-matrix/description/
import timeit


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and matrix[0] + self.spiralOrder(self.__ccw_rotate(matrix[1:]))

    @staticmethod
    def __ccw_rotate(matrix):
        return list(map(list, zip(*[reversed(row) for row in matrix])))


def run():
    Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)


if __name__ == '__main__':
    main()
