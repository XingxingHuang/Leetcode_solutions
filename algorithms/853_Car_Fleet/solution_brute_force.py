from fractions import Fraction


class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        brute force simulate the prcess, time exceeded
        good thing is that we know how many cars in one fleet
        """
        if len(position) != len(speed):
            return 0
        if len(position) == 0:
            return 0
        max_speed = max(speed)
        speed = [Fraction(s, max_speed) for s in speed]
        fleets = sorted(zip(position, speed, [1] * len(speed)), key=lambda x: x[0], reverse=True)
        fleets = [list(fleet) for fleet in fleets]
        total_fleet = 0
        while fleets:
            # print(fleets, total_fleet)
            for idx, fleet in enumerate(fleets):
                fleet[0] = min(target, fleet[1] + fleet[0])
                if idx >= 1:
                    fleet[0] = min(fleets[idx - 1][0], fleet[0])

            # print(fleets)

            idx = 0
            while idx < len(fleets) - 1 and len(fleets) >= 2:
                # print(idx, fleets)
                if fleets[idx + 1][0] >= fleets[idx][0]:
                    fleets[idx][2] += fleets[idx + 1][2]
                    fleets.pop(idx + 1)
                else:
                    idx += 1

            for fleet in fleets:
                # print(fleet, fleet[0], target)
                if fleet[0] == target:
                    total_fleet += 1
                    fleets.remove(fleet)
        # print(total_fleet)
        return total_fleet







