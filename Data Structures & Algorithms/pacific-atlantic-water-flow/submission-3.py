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
        pacific_visited = set()
        atlantic_visited = set()

        def bfs(r, c, ocean_set) -> None:
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and 
                        col in range(COLS) and
                        (row, col) not in ocean_set and
                        heights[row][col] >= heights[r][c]):
                        # if >=, cell can reach ocean from there
                        # since we start from cells next to ocean
                        q.append((row, col))
                        ocean_set.add((row, col))
        
        # pacific cells
        for i in range(COLS):
            if (0, i) not in pacific_visited:
                pacific_visited.add((0, i))
                bfs(0, i, pacific_visited)
        for i in range(ROWS):
            if (i, 0) not in pacific_visited:
                pacific_visited.add((i, 0))
                bfs(i, 0, pacific_visited)
        
        # atlantic cells
        for i in range(COLS):
            if (ROWS - 1, i) not in atlantic_visited:
                atlantic_visited.add((ROWS - 1, i))
                bfs(ROWS - 1, i, atlantic_visited)
        for i in range(ROWS):
            if (i, COLS - 1) not in atlantic_visited:
                atlantic_visited.add((i, COLS - 1))
                bfs(i, COLS - 1, atlantic_visited)

        return [list(t) for t in pacific_visited & atlantic_visited]


