class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs graph traversal
        # level order traversal

        # count fresh fruit
        # setup for the level order traversal - add rotten to a queue

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        freshCount = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        minutes = 0
        while q and freshCount > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2       # infected
                        freshCount -= 1
                        q.append((nr, nc))
            minutes += 1
        
        return minutes if freshCount == 0 else -1







