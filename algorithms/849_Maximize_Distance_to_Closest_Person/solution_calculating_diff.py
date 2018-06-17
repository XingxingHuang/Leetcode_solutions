import math


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        people = [i for i, seat in enumerate(seats) if seat]
        if seats[0] == 0:
            people = [-people[0]] + people
        if seats[-1] == 0:
            people = people + [2 * len(seats) - people[-1] - 2]
        max_dis = 0
        for i in range(len(people) - 1):
            max_dis = max(max_dis, math.ceil((people[i + 1] - people[i] - 1) / 2))
        return max_dis


