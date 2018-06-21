class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permutation = []
        symbols = dict()
        for num in nums:
            if num in symbols:
                symbols[num] += 1
            else:
                symbols[num] = 1
        self._backtracking([], symbols)
        return self.permutation

    def _backtracking(self, current_set, remaining_symbols):
        if not remaining_symbols:
            self.permutation.append(current_set)
        else:
            for key in remaining_symbols:
                self._backtracking(current_set + [key], self.update_dict(remaining_symbols, key))

    def update_dict(self, symbols, key):
        dic = symbols.copy()
        dic[key] -= 1
        if dic[key] == 0:
            del dic[key]
        return dic

