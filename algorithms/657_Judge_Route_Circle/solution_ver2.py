# https://leetcode.com/problems/judge-route-circle/description/
import timeit

class Solution:
    def __init__(self):
        self.h = 0
        self.v = 0

    def move(self, direction):
        if direction == "L":
            self.h += 1
        if direction == "R":
            self.h -= 1
        if direction == "U":
            self.v += 1
        if direction == "D":
            self.v -= 1

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        for direction in moves:
            self.move(direction)
        return self.h == 0 and self.v == 0

def run():
    Solution().judgeCircle("UUUDDDLLLRRR")

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(100000)
    print(t)

if __name__ == '__main__':
    main()
