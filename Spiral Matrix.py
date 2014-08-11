class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == [] or matrix[0] == []:
            return result
        m,n = len(matrix), len(matrix[0])
        while (m != 1 or n != 1):
            if m == 1:
                result += matrix[0]
                break
            if n == 1:
                result += [matrix[i][0] for i in range(len(matrix))]
                break
            # outter top
            for i in range(n):
                result.append(matrix[0][i])
            # outter right
            for i in range(1,m):
                result.append(matrix[i][n-1])
            # outter bottom
            for i in range(1,n):
                result.append(matrix[m-1][n-1-i])
            # outter left
            for i in range(1,m-1):
                result.append(matrix[m-1-i][0])
            # reduce the current matrix into its inner matrix
            matrix = [[matrix[i][j] for j in range(1,n-1)] for i in range(1,m-1)]
            # update number of rows and columns
            if matrix == [] or matrix[0]==[]:
                break
            else:
                m,n = len(matrix), len(matrix[0])
        # only 1 element left
        if m == 1 and n == 1:
            result.append(matrix[0][0])
        return result

if __name__ == "__main__":
    slt = Solution()
    print slt.spiralOrder([]) == []
    print slt.spiralOrder([[1]]) == [1]
    print slt.spiralOrder([[1],[2]]) ==[1,2]
    print slt.spiralOrder([[1,2]]) == [1,2]
    print slt.spiralOrder([[1,2],[1,2]]) == [1,2,2,1]
    print slt.spiralOrder([[1,2,3],[1,2,3],[1,2,3]]) == [1,2,3,3,3,2,1,1,2]
    print slt.spiralOrder([[1,2,3],[1,2,3],[1,2,3],[1,2,3]]) == [1,2,3,3,3,3,2,1,1,1,2,2]
    print slt.spiralOrder([[1,2,3,4],[1,2,3,4],[1,2,3,4]]) == [1,2,3,4,4,4,3,2,1,1,2,3]
    
    
    
