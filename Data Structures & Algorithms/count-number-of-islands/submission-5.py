class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # A bfs will fully search an island

        ROWS, COLS = len(grid), len(grid[0])

        islandCount = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def bfs(row: int, col: int):
            q = deque()
            grid[row][col] = "0"
            q.append((row, col))
            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == "0"):
                        continue
                    grid[nr][nc] = "0"    # set to 0 and add to queue for processing
                    q.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islandCount += 1

        return islandCount


