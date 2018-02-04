# https://leetcode.com/problems/jewels-and-stones/description/
import timeit

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # return sum([1 for char in S if char in J])
        # return sum(map(S.count, J))
        return sum(map(J.count, S))

def run():
    J = "aA"
    S = "aAAbbbb"
    Solution().numJewelsInStones(J, S)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
