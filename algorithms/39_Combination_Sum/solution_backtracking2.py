# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self._candidates = sorted(candidates)
        self._result = []
        self._backtracking(target, [], 0)
        return self._result

    def _backtracking(self, target, numbers, idx):
        exceed = False
        for i in range(idx, len(self._candidates)):
            if exceed:
                return
            numbers.append(self._candidates[i])
            if target - self._candidates[i] > 0:
                self._backtracking(target - self._candidates[i], numbers, i)
            elif target - self._candidates[i] == 0:
                self._result.append(list(numbers))
                exceed = True
            else:
                exceed = True
            numbers.pop()
        return