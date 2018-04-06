# https://leetcode.com/problems/partition-labels/description/


class Solution(object):
    def partitionLabels(self, S):
        """
        :param S: string to partition on
        :return: list of consecutive number of chars to group on
        """
        char_last_locations = {char: idx for idx, char in enumerate(S)}
        head, tail = 0, 0
        partitions = []
        for idx, char in enumerate(S):
            tail = max(tail, char_last_locations[char])
            if idx == tail:
                partitions.append(idx - head + 1)
                head = idx + 1
        return partitions
