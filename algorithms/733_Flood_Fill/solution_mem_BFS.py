class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        nr, nc = len(image), len(image[0])

        def valid_loc(r,c):
            return 0 <= r < nr and 0 <= c < nc

        old_color = image[sr][sc]
        image[sr][sc] = newColor
        stack = [(sr, sc)]
        visited = set((sr, sc))
        while stack:
            r, c = stack.pop()
            for dr, dc in [[-1,0], [1, 0], [0, 1], [0, -1]]:
                if not valid_loc(r+dr, c+dc) or (r+dr, c+dc) in visited:
                    continue
                visited.add((r+dr, c+dc))
                if image[r+dr][c+dc] == old_color:
                    image[r+dr][c+dc] = newColor
                    stack.append((r+dr, c+dc))
        return image



if __name__ == '__main__':
    assert Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc =1, newColor=2) == [[2,2,2],[2,2,0],[2,0,1]], 'testcase fail'
