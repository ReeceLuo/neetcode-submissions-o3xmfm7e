class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # brute force - bfs from each cell, mark if can flow in pacific
        # and atlantic
        # m x n x m x n

        # better - do graph traversal from top/left cells to heights equal
        # or greater to get cells that can reach pacific. Do graph traversal
        # from bottom/right cells to heights equal aor greater to get cells 
        # that can reach atlantic. Cells in both are returned.
        
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(coordinates, ocean):
            q = deque(coordinates)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and
                        col in range(COLS) and
                        not ocean[row][col] and
                        heights[row][col] >= heights[r][c]):
                        q.append((row, col))

        pacific = []
        atlantic = []

        for i in range(ROWS):
            pacific.append((i, 0))
            atlantic.append((i, COLS - 1))
        for i in range(COLS):
            pacific.append((0, i))
            atlantic.append((ROWS - 1, i))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        
        return res



