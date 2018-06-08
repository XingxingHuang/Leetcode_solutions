# https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
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