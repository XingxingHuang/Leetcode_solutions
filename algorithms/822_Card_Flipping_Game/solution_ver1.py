# https://leetcode.com/problems/card-flipping-game/description/


class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        # time limit exceed
        """
        good = []
        combs = set(zip(fronts, backs))
        for comb in combs:
            if comb[0] != comb[1]:
                rest = set(c for c in combs if c != comb)
                for num in comb:
                    if all(any(num != e for e in c) for c in rest):
                        good.append(num)
        return min(good) if good else 0
