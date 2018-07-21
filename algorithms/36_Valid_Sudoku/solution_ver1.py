class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def check_valid_row(row):
            row_no_na = [ele for ele in row if ele in '123456789']
            return len(set(row_no_na)) == len(row_no_na)

        def check_valid_row_by_idx(row_idx):
            row = board[row_idx]
            return check_valid_row(row)

        def check_valid_col_by_idx(col_idx):
            row = [board[r][col_idx] for r in range(9)]
            return check_valid_row(row)

        def check_valid_grid(row_start, col_start):
            row = [board[r][c] for r in range(row_start, row_start + 3) for c in range(col_start, col_start + 3)]
            return check_valid_row(row)

        for idx in range(9):
            if not check_valid_row_by_idx(idx):
                return False
            if not check_valid_col_by_idx(idx):
                return False

        for row_start in [0, 3, 6]:
            for col_start in [0, 3, 6]:
                if not check_valid_grid(row_start, col_start):
                    return False

        return True

