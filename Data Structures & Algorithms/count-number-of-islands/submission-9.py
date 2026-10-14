class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # breadth first search, set explored to 0

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == "0"):
                        continue
                    # otherwise, valid, land cell
                    grid[nr][nc] = "0"
                    q.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        
        return res