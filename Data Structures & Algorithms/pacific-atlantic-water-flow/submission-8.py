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

        def add_cell(r, c, ocean):
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        heights[nr][nc] >= heights[r][c] and
                        not ocean[nr][nc]):
                        q.append((nr, nc))
                        
        # top/bottom cells
        for i in range(COLS):
            add_cell(0, i, pac)
            add_cell(ROWS - 1, i, atl)
        # left/right cells
        for i in range(ROWS):
            add_cell(i, 0, pac)
            add_cell(i, COLS - 1, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res

