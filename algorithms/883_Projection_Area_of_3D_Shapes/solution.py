class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area_xy = sum(len([e for e in row if e != 0]) for row in grid)
        area_xz = sum(max(col) for col in zip(*grid))
        area_yz = sum(max(row) for row in grid)
        return area_xy + area_xz + area_yz


if __name__ == '__main__':
    inputs = [[[1, 2], [3, 4]], [[2]], [[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    outputs = [17, 5, 14]
    for input, output in zip(inputs, outputs):
        solution = Solution().projectionArea(input)
        if solution != output:
            print('failed input {} expected {} but got {}'.
                  format(input, output, solution))
