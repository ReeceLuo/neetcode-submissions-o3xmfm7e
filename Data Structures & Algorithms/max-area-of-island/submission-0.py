class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            currArea = 1

            while q:
                rows, cols = q.popleft()
                for dr, dc in directions:
                    nr, nc = rows + dr, cols + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    currArea += 1
                    grid[nr][nc] = 0
                    q.append((nr, nc))
            return currArea



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea




