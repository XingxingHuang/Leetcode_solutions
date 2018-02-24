# https://leetcode.com/problems/island-perimeter/description/
import timeit

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # brute one pass scan
        r, c = len(grid), len(grid[0])
        s = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    s += 4
                    if i < r - 1:
                        if grid[i+1][j] == 1:
                            s -= 2
                    if j < c - 1:
                        if grid[i][j+1] == 1:
                            s -= 2
        return s


def run():
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    Solution().islandPerimeter(grid)


def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)


if __name__ == '__main__':
    main()


