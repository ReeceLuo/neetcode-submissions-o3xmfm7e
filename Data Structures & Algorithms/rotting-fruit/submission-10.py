class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # all fresh adjacent to rotten will rot each level
        # must do multi source bfs

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:    # fresh
                    fresh += 1
                elif grid[r][c] == 2:  # rotten
                    q.append((r, c))

        time = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1

        return time if 0 == fresh else -1


