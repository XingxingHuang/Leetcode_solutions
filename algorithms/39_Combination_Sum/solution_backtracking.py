# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        numbers = []
        self._backtracking(results, numbers, candidates, target)
        return results

    def _backtracking(self, results, numbers, candidates, target):
        if sum(numbers) == target:
            numbers.sort()
            if numbers not in results:
                results.append(numbers)
        elif sum(numbers) > target:
            return
        else:
            for num in candidates:
                self._backtracking(results, numbers + [num], candidates, target)
