class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Fill in each row at a time, iterating across each columns.
        # If cell is free, place queen and go on to next row.
            # when rows == n, append and return

        # base case - 
        # decision
        # constraint - queens cannot be adjacent diagonal/horizontal/vertical
        # backtracking

        res = []
        board = [["."] * n for _ in range(n)]

        def checkSafe(r, c, board):
            # we know same row is safe since we only put one as we iterate
            # so we just need to check column and diagonals
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1
            
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            
            return True

        def backtrack(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # since we place queens row by row, iterate across each
            # column. 
            for c in range(n):
                if checkSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
            
        backtrack(0)
        return res        
                    

