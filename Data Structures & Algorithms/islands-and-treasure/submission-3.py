class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # brute force - do a bfs from each land cell until we reach 
        # a treasure chest - O(m x n x m x n)

        # better - do a multi-source simultaneous bfs from each treasure chest, filling in the land cells

        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        level = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == INF):
                        grid[nr][nc] = level
                        q.append((nr, nc))
            level += 1
        
