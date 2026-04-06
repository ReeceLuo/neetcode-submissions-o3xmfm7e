class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        # during bfs, we must check every direction from the current element
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        def bfs(r, c):
            q = deque()         # two sided q
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # don't add to bfs if "0" or if index is out of bounds
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS
                        or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
                
        for r in range(ROWS):
            for c in range(COLS):
                # For each element that equals 1, run bfs
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands
