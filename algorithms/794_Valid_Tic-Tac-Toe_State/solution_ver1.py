class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x_counts = "".join(board).count('X')
        o_counts = "".join(board).count('O')
        x_wins = self.__wins(board, 'X')
        o_wins = self.__wins(board, 'O')
        if x_wins == 1 and o_wins == 0 and x_counts - o_counts == 1:
            return True
        elif x_wins == 0 and o_wins == 1 and  x_counts == o_counts:
            return True
        elif x_wins == 0 and o_wins == 0 and (x_counts - o_counts) in [0, 1]:
            return True
        return False

    @staticmethod
    def __wins(board, symbol):
        return sum(list(map(lambda row: row == symbol * 3,
                board +
                list(map(lambda row: "".join(row), zip(*board))) +
                ["".join([board[i][i] for i in range(len(board))])] +
                ["".join([board[i][len(board) - i - 1] for i in range(len(board))])]
            )))
