class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # every minute, a rotten fruit infects fresh fruit
        # count every fresh fruit
        # do level-order bfs from rotten fruits


        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        freshCount = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:   # fresh
                    freshCount += 1
                elif grid[r][c] == 2: # rotten
                    q.append((r, c))

        time = 0
        while q and freshCount > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        freshCount -= 1
                        q.append((nr, nc))

            time += 1

        return time if freshCount == 0 else -1


            
