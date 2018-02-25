class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        step = self.__l1([0, 0], target)
        steps = [self.__l1(ghost, target) for ghost in ghosts]
        if min(steps) <= step:
            return False
        return True

    @staticmethod
    def __l1(p1, p2):
        return sum(map(lambda pp: abs(pp[0] - pp[1]), zip(p1, p2)))