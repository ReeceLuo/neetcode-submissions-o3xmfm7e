class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        maxArea = 0

        def bfs(r, c) -> int:
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    area += 1
                    q.append((nr, nc))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)
        
        return maxArea

