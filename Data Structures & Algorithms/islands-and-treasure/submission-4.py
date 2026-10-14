class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # brute force - perform some graph traversal from each land cell
        # O(m x n x m x n) for m x n land cells

        # better - perform level-order bfs (simulataneous) from each treasure chest to land
        # whichever chest reaches land first is the closest

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        INF = 2147483647

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == INF):
                        grid[nr][nc] = dist
                        q.append((nr, nc))
            dist += 1








