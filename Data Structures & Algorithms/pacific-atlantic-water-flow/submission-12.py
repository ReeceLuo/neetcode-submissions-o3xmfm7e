class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # water can flow to adjacent cells to height equal or lower
        # can flow into the ocean
        # find cells that can flow to both pacific and atlantic

        # brute force - do bfs from each cell, when it reaches the pacific and atlantic, return a boolean for each
        # better - do a bfs from pacific-bordering cells, mark cells it reaches. do bfs from atlantic-bordering cells, mark cells it reaches. Return cells in both.
        # use sets to prevent revisiting cells. 
        
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]
        pac_visited = set()
        atl_visited = set()

        def bfs(cells, ocean, visited):
            for r, c in cells:
                visited.add((r, c))
                ocean[r][c] = True
            
            q = deque(cells)
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visited or
                        heights[nr][nc] < heights[r][c]):
                        continue
                    visited.add((nr, nc))
                    ocean[nr][nc] = True
                    q.append((nr, nc))

        pac_cells = []
        atl_cells = []
        for r in range(ROWS):
            pac_cells.append((r, 0))
            atl_cells.append((r, COLS - 1))
        for c in range(COLS):
            pac_cells.append((0, c))
            atl_cells.append((ROWS - 1, c))

        bfs(pac_cells, pac, pac_visited)
        bfs(atl_cells, atl, atl_visited)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] == True and atl[r][c] == True:
                    res.append([r, c])

        return res



        
        
