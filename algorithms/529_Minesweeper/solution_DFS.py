class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        nr, nc = len(board), len(board[0])
        seen = set()
        stack = [click]

        def check_valid_pos(r, c):
            return 0 <= r < nr and 0 <= c < nc

        def check_num_srounding_mines(r, c):
            total_mines = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0:
                        continue
                    if check_valid_pos(r + dr, c + dc):
                        total_mines += board[r + dr][c + dc] in 'MX'
            return total_mines

        while stack:
            r, c = stack.pop()
            if board[r][c] == 'M':
                board[r][c] = 'X'
            # print(seen)
            # pprint(board)
            else:
                num_srounding_mines = check_num_srounding_mines(r, c)
                if num_srounding_mines > 0:
                    board[r][c] = str(num_srounding_mines)
                else:
                    board[r][c] = 'B'
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
                        if check_valid_pos(r + dr, c + dc):
                            if board[r + dr][c + dc] in 'ME' and (r + dr, c + dc) not in seen:
                                stack.append([r + dr, c + dc])
                                # pprint(board)
        return board

