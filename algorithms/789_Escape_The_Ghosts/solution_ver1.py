# https://leetcode.com/problems/escape-the-ghosts/description/

class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        return all(map(lambda ghost: self.__l1(ghost, target) > self.__l1([0,0], target), ghosts))

    @staticmethod
    def __l1(p1, p2):
        return sum(map(lambda pp: abs(pp[0] - pp[1]), zip(p1, p2)))