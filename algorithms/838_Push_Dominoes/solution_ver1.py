# https://leetcode.com/problems/push-dominoes/description/


class Solution(object):
    @staticmethod
    def _map_force_to_direction(net_force):
        if net_force > 0:
            return 'R'
        if net_force < 0:
            return 'L'
        return '.'

    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        num_dominoes = len(dominoes)
        net_forces = [0] * num_dominoes
        current_right_force = 0
        for idx, direction in enumerate(dominoes):
            if direction == 'R':
                current_right_force = num_dominoes
            if direction == 'L':
                current_right_force = 0
            if direction == '.':
                current_right_force = max(current_right_force - 1, 0)
            net_forces[idx] += current_right_force

        current_left_force = 0
        for idx, direction in enumerate(dominoes[::-1]):
            if direction == 'L':
                current_left_force = num_dominoes
            if direction == 'R':
                current_left_force = 0
            if direction == '.':
                current_left_force = max(current_left_force - 1, 0)
            net_forces[num_dominoes - idx - 1] -= current_left_force

        return "".join(map(self._map_force_to_direction, net_forces))
