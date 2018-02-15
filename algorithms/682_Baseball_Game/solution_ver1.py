# https://leetcode.com/problems/baseball-game/description/
import timeit

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if len(ops) == 1:
            return int(ops[0])
        else:
            history = []
            for op in ops:
                if op not in ['C', 'D', '+']:
                    history.append(int(op))
                elif op == 'C':
                    history.pop()
                elif op == 'D':
                    history.append( 2 * history[-1])
                elif op == '+':
                    history.append(history[-1] + history[-2])
            return sum(history)


def run():
    Solution().calPoints(["5","-2","4","C","D","9","+","+"])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
