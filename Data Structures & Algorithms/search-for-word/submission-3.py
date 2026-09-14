class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # base case - stop exploring when:
            # word found
            # len curr == word
            # index invalid

        # choice - add letter if correct, then mark visited

        # constraint - word must be present horizontally / vertically
        # and same cell cannot be used more than once
        #

        # backtrack - unmark visited

        # we need to use an index to track which letter we are currently at

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i, r, c):
            if i >= len(word):
                return True
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS 
                or board[r][c] != word[i] or
                (r, c) in visited):
                return False
            
            visited.add((r, c))

            found = (dfs(i + 1, r + 1, c) or
                     dfs(i + 1, r - 1, c) or
                     dfs(i + 1, r, c + 1) or
                     dfs(i + 1, r, c - 1))
            
            visited.remove((r, c))
            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        
        return False








