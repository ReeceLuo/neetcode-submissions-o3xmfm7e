class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # each minute, adjacent fruits are "infected"
        # this is a BFS since we are exploring by levels

        # count fresh fruit
        # run bfs on each rotten fruit simultaneously
        # once complete, if total does not equal fresh fruit,
        # then not possible

        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and 
                        col in range(COLS) and
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1



