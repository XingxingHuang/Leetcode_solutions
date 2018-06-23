class Solution:
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        self._visited = set()
        self._num_islands = 0
        self._nr = len(grid)
        self._nc = len(grid[0])
        self._grid = grid
        for r in range(self._nr):
            for c in range(self._nc):
                if (self._grid[r][c] == "1") and ((r, c) not in self._visited):
                    self._num_islands += 1
                    self._searchLandDfs(r, c)
        return self._num_islands

    def valid_rc(self, r, c):
        return 0 <= r < self._nr and 0 <= c < self._nc

    def _searchLandDfs(self, r, c):
        self._visited.add((r, c))
        for rdelta, cdelta in self.moves:
            rr, cc = r + rdelta, c + cdelta
            if self.valid_rc(rr, cc):
                if (rr, cc) not in self._visited:
                    if self._grid[rr][cc] == '1':
                        self._searchLandDfs(rr, cc)

