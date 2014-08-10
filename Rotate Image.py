class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [[matrix[len(matrix)-1-i][j] for i in range(len(matrix))] for j in range(len(matrix))]
