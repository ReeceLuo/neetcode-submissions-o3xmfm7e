class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # base case - stop exploring if string length == word
        # go through each cell and try
        # backtracking - go back to previous letter (index)

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, currIndex):
            if currIndex == len(word):
                return True
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[currIndex] or
                (r, c) in visited):
                return False
            
            visited.add((r, c))
            res = (dfs(r + 1, c, currIndex + 1) or
                   dfs(r - 1, c, currIndex + 1) or
                   dfs(r, c + 1, currIndex + 1) or
                   dfs(r, c - 1, currIndex + 1))
            visited.remove((r, c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
