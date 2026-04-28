class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # bfs for island that tracks area
        def bfs(row: int, col: int) -> int:
            area = 1
            q = deque()
            grid[row][col] = 0
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    area += 1

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
    
        return maxArea


