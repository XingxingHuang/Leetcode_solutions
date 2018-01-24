class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: return []
        result = [[1]]
        i = 1
        while i < numRows:
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1]+result[i-1][j])
            result.append(row)
            i += 1
        return result
