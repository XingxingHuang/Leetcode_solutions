# https://leetcode.com/problems/card-flipping-game/description/


class Solution(object):
    """
    :type fronts: List[int]
    :type backs: List[int]
    :rtype: int
    accepted
    for cards with same number on both sides, its always bad
    if a number is not in the set of bad numbers, since we can flip cards any
    number of times, we can always create a situation for this number to be
    good.
    """
    def flipgame(self, fronts, backs):
        bad_num = set(i for i, j in zip(fronts, backs) if i == j)
        return min([num for num in fronts + backs if num not in bad_num],
                   default=0)

