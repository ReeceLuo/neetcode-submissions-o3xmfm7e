class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # must do multi-level bfs since each rotten infects its neighbors
        # at the same time
        # runtime: O(m x n) - each fresh can only be processed once
        # space: O(m x n) for queue

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # count the number of fresh fruits and add rotten to queue for bfs.
        # if total infected at the end equals
        # the count of fresh, then it is possible
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        infected = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1








