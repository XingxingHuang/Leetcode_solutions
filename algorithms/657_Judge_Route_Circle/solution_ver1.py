# https://leetcode.com/problems/judge-route-circle/description/
import timeit

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count("L") == moves.count("R")) and (moves.count("U") == moves.count("D"))

def run():
    Solution().judgeCircle("UUUDDDLLLRRR")

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(100000)
    print(t)

if __name__ == '__main__':
    main()
