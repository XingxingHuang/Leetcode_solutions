# https://leetcode.com/problems/soup-servings/description/
import random


class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        #### time exceeded
        """
        experiments = [self.game(N) for _ in range(655355)]
        return sum(experiments) / len(experiments)

    @staticmethod
    def game(N):
        A, B = N, N
        while A != 0 and B != 0:
            # print(A, B)
            choice = random.randint(1, 5)
            if choice == 1:
                A = max(0, A - 100)
            if choice == 2:
                A = max(0, A - 75)
                B = max(0, B - 25)
            if choice == 3:
                A = max(0, A - 50)
                B = max(0, B - 50)
            if choice == 4:
                A = max(0, A - 25)
                B = max(0, B - 75)
            if A == 0 and B != 0:
                return 1
            if A == 0 and B == 0:
                return 0.5
        return 0
