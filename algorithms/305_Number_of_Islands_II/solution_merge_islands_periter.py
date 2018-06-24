class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        # time limit exceeds
        """
        self._pos_island_mapping = dict()
        island_id = 1
        results = []
        for r, c in positions:
            if (r, c) not in self._pos_island_mapping:
                self._pos_island_mapping[(r, c)] = island_id
                island_idx = [island_id]
                island_id += 1
                # upper
                if r - 1 >= 0 and (r - 1, c) in self._pos_island_mapping:
                    island_idx.append(self._pos_island_mapping[(r - 1, c)])
                # lower
                if r + 1 < m and (r + 1, c) in self._pos_island_mapping:
                    island_idx.append(self._pos_island_mapping[(r + 1, c)])
                # left
                if c - 1 >= 0 and (r, c - 1) in self._pos_island_mapping:
                    island_idx.append(self._pos_island_mapping[(r, c - 1)])
                # right
                if c + 1 < n and (r, c + 1) in self._pos_island_mapping:
                    island_idx.append(self._pos_island_mapping[(r, c + 1)])
                island_idx = set(island_idx)
                if len(island_idx) > 1:
                    self.merge_islands(island_idx)
            results.append(len(set(self._pos_island_mapping.values())))
        return results

    def merge_islands(self, island_idx):
        min_idx = min(island_idx)
        for pos in self._pos_island_mapping:
            if self._pos_island_mapping[pos] in island_idx:
                self._pos_island_mapping[pos] = min_idx
