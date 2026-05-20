class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # each minute, adjacent fruits are "infected"
        # this is a BFS since we are exploring by levels

        # count fresh fruit
        # run bfs on each rotten fruit simultaneously
        # once complete, if total does not equal fresh fruit,
        # then not possible

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        fresh = 0
        q = deque() # rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        self.infected = 0

        def addCell(self, row, col):
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row, col) in visited or
                grid[row][col] == 0 or
                grid[row][col] == 2):
                return 0
            visited.add((row, col))
            q.append((row, col))
            self.infected += 1
            return 1

        minutes = 0
        while q:
            change = 0
            for i in range(len(q)):
                r, c = q.popleft()
                change += addCell(self, r + 1, c)
                change += addCell(self, r - 1, c)
                change += addCell(self, r, c + 1)
                change += addCell(self, r, c - 1)
            if change > 0:
                minutes += 1
            else:
                break

        if self.infected == fresh:
            return minutes
        else:
            return -1
            





        