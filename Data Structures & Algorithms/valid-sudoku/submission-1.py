class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            row_nums = []
            for c in range(cols):
                if board[r][c] in row_nums:
                    return False
                if board[r][c] != ".":
                    row_nums.append(board[r][c])
        
        for c in range(cols):
            col_nums = []
            for r in range(rows):
                if board[r][c] in col_nums:
                    return False
                if board[r][c] != ".":
                    col_nums.append(board[r][c])

        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                mini_board = []
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        if board[r][c] in mini_board:
                            return False
                        if board[r][c] != ".":
                            mini_board.append(board[r][c])
                            
        return True

