# from collections import defaultdict


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # groups = defaultdict(list)
        pairs = []
        i, j, current_char = 0, 0, S[0]
        while j < len(S):
            if S[j] != current_char:
                if j - i >= 3:
                    # groups[current_char*(j - i)].append([i,j-1])
                    pairs.append((current_char * (j - i), [i, j - 1]))
                current_char = S[j]
                i = j
            j += 1
        if j - i >= 3:
            pairs.append((current_char * (j - i), [i, j - 1]))

        # pairs.sort(key=lambda x: x[0])
        return [x[1] for x in pairs]
