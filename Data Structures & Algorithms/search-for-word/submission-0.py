class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # base case - stop exploring if string length == word
        # go through each cell and try
        # backtracking - go back to previous letter (index)

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        res = []
        def dfs(r, c, currIndex):
            if currIndex == len(word) - 1:
                res.append(1)
                return
            
            visited.add((r, c))
            currIndex += 1
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    board[nr][nc] == word[currIndex]):
                    dfs(nr, nc, currIndex)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    dfs(r, c, 0)
        
        return len(res) > 0
