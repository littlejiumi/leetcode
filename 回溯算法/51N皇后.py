class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)] # [[".","."],[".","."]]
        res = []
        def isVaild(board, row, col):
            #判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            i = row-1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i = row-1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        def backtrack(board, row, n):
            if row == n:
                path = []
                for i in board:
                    temp_str = "".join(i)
                    path.append(temp_str)
                res.append(path)
            for col in range(n):
                if not isVaild(board, row, col): continue
                board[row][col] = 'Q'
                backtrack(board, row+1, n)
                board[row][col] = '.'
        backtrack(board, 0, n)
        return res
