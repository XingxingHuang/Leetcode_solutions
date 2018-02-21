# https://leetcode.com/problems/distribute-candies/description/
import timeit

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        unique_candies = set(candies)
        if len(unique_candies) >= len(candies) // 2:
            return len(candies) // 2
        else:
            return len(unique_candies)

def run():
    Solution().distributeCandies([1,1,2,2,3,3])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()