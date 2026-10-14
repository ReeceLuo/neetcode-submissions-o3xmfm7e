class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # return true if word is in grid, otherwise false
        # must use dfs w/ backtracking and must keep track of current letter (index)
            # base case - stop exploring when end of word or invalid index
            # decision - continue exploring or not
            # constraint - no cell used more than once
            # backtrack - mark cell as not visited
        
        # keep track of visited with set

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i >= len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS 
                or (r, c) in visited or
                board[r][c] != word[i]):
                return False

            visited.add((r, c))
            exists = (dfs(r + 1, c, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r, c - 1, i + 1))

            visited.remove((r, c))
            return exists
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
        

