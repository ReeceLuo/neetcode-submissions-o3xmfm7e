class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # when reaching an island, perform bfs to adjacent

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0

        def bfs(self, x, y):
            q = deque()
            q.append((x, y))
            grid[x][y] = "0"
            while q:
                x, y = q.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or ny < 0 or
                        nx >= ROWS or ny >= COLS or
                        grid[nx][ny] == "0"):
                        continue
                    grid[nx][ny] = "0"
                    q.append((nx, ny))
            return

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == "1":
                    bfs(self, x, y)
                    count += 1
        
        return count



