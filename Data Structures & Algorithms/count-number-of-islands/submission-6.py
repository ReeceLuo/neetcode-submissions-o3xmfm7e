class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        num_islands = 0

        def dfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == "0"):
                return
            visited.add((r, c))
            grid[r][c] = "0"
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    dfs(r, c)

        return num_islands