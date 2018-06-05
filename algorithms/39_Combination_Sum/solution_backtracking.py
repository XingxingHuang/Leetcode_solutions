# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        numbers = []
        self._results = []
        self._backtracking(numbers, candidates, target)
        return self._results

    def _backtracking(self, numbers, candidates, target):
        if sum(numbers) == target:
            numbers.sort()
            if numbers not in self._results:
                self._results.append(numbers)
        elif sum(numbers) > target:
            return
        else:
            for num in candidates:
                self._backtracking(numbers + [num], candidates, target)
