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
        q = deque()
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        self.rotten_count = 0

        def add_cell(self, r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0
            visited.add((r, c))
            q.append((r, c))
            self.rotten_count += 1
            return 1
        
        # end bfs when no fruit is infeced
        min_minutes = 0
        while q:
            change = 0
            for i in range(len(q)):
                r, c = q.popleft()
                change += add_cell(self, r + 1, c)
                change += add_cell(self, r - 1, c)
                change += add_cell(self, r, c + 1)
                change += add_cell(self, r, c - 1)
            if not change:
                break
            min_minutes += 1

        if fresh_count == self.rotten_count:
            return min_minutes
        return -1
        





