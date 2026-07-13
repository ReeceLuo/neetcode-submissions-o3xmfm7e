class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # brute force - perform a graph traversal at each land cell
        # to closest treasure chest and fill
            # runtime: O(m x n x m x n)
            # space: O(1)

        # better: start from each treasure chest and perform multi level bfs
            # more efficient and keeps unreachable INF cells as INF

        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == INF):
                        grid[nr][nc] = level
                        q.append((nr, nc))



