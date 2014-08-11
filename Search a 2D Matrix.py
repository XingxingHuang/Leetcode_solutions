class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return False
        heads = [matrix[i][0] for i in range(len(matrix))]
        heads = [i > target for i in heads]
        row = 0
        if True in heads:
            row = heads.index(True)-1
        else:
            row = len(matrix)-1
        if target in matrix[row]:
            return True
        else:
            return False
