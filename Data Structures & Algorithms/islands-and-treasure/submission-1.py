class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # brute force: run bfs at each INF square to find distance
        # - O (m x n x m x n) time
            # creates inconsistency (order matters)
        # bfs from gates (chests) simultaneously

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        def addCell(r, c):
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visited or
                grid[r][c] == -1):
                return
            visited.add((r, c))
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1



        