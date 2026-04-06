class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):      # bfs iterative implementation with queue
            q = deque()     # double sided queue
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                row, col = q.popleft() # pop from front of queue
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or 
                        nr >= rows or nc >= cols or
                        grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
                

    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # is island, run bfs
                    bfs(r, c)
                    islands += 1

        return islands
