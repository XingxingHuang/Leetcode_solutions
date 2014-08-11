class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if matrix == [] or matrix[0] == []:
            return []
        m,n = len(matrix), len(matrix[0])
        r,c = -1,-1
        # find a zero in matrix
        for i in range(m):
            for j in range(n):
                # if a zero found then use the column and row as reference
                if matrix[i][j] == 0:
                    r,c = i,j
                    break
            if r != -1:
                break
        # set rows and columns to zeros
        if r != -1:
            # mark up rows and columns needed to set to zero in the reference row and column
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        matrix[r][j] = 0
                        matrix[i][c] = 0
            # set columns to zeros
            for j in range(n):
                if matrix[r][j] == 0 and j != c:
                    for k in range(m):
                        matrix[k][j] = 0
            # set rows to zeros
            for i in range(m):
                if matrix[i][c] == 0 and i != r:
                    matrix[i] = [0 for k in range(n)]
            matrix[r] = [0 for i in range(n)]
            for i in range(m):
                matrix[i][c] =0
            
        return matrix
                    
                    

if __name__ == "__main__":
    slt = Solution()
    print "test 0 matrix"
    matrix = []
    for i in matrix: print i
    print "output"
    matrix = slt.setZeroes(matrix)
    for i in matrix: print i
    
    print "test 1 matrix"
    matrix = [[0]]
    for i in matrix: print i
    print "output"
    matrix = slt.setZeroes(matrix)
    for i in matrix: print i
    
    print "test 2 matrix"
    matrix = [[1,2],[0,1]]
    for i in matrix: print i
    print "output"
    matrix = slt.setZeroes(matrix)
    for i in matrix: print i
    print "test 3 matrix"
    matrix = [[1,2],[0,1],[1,0]]
    for i in matrix: print i
    print "output"
    matrix = slt.setZeroes(matrix)
    for i in matrix: print i
    matrix = [[1,2,3],[1,0,1],[1,1,1]]
    for i in matrix: print i
    print "output"
    matrix = slt.setZeroes(matrix)
    for i in matrix: print i
