# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        # rotate matrix layer by layer
        """
        total_layers = len(matrix) // 2
        for layer_num in range(total_layers):
            self._rotate_layer(matrix, layer_num, len(matrix) - 2 * layer_num)

    def _rotate_layer(self, matrix, layer_num, matrix_dim):
        for elem in range(matrix_dim - 1):
            temp = matrix[layer_num][layer_num + elem]
            matrix[layer_num][layer_num + elem] = \
                matrix[layer_num + matrix_dim - 1 - elem][layer_num]
            matrix[layer_num + matrix_dim - 1 - elem][layer_num] =\
                matrix[layer_num + matrix_dim - 1][layer_num + matrix_dim - 1 - elem]
            matrix[layer_num + matrix_dim - 1][layer_num + matrix_dim - 1 - elem] = \
                matrix[layer_num + elem][layer_num + matrix_dim - 1]
            matrix[layer_num + elem][layer_num + matrix_dim - 1] = temp
