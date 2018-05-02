# https://leetcode.com/problems/friends-of-appropriate-ages/description/
from collections import defaultdict


def endzone(a, b):
    return any([a <= 0.5 * b + 7, a > b, (a > 100) and (b < 100)])


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        brute force on combination of ages.
        """
        age_counts = defaultdict(int)
        for age in ages:
            age_counts[age] += 1
        total = 0
        for age_a in age_counts:
            for age_b in age_counts:
                if not endzone(age_a, age_b):
                    total += age_counts[age_a] * age_counts[age_b]
                    if age_a == age_b:
                        total -= age_counts[age_a]
        return total
