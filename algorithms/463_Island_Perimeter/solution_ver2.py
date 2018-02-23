# https://leetcode.com/problems/island-perimeter/description/
import timeit

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # this is much much faster then the brute force scan
        def islandPerimeter(self, grid):
            return sum(
                        sum(map(operator.ne, [0] + row, row + [0]))   # this calculates the number of edge in a row
                        for row in grid + list(map(list, zip(*grid))) # appending matrix with its transpose so
                                                                      # we are calculating both edge in row and column!
                )

def run():
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    Solution().islandPerimeter(grid)


def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)


if __name__ == '__main__':
    main()


