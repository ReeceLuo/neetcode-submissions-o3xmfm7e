class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # do some graph traversal
        # explore all adjacent directions
            # if land, add and continue
            # if not, add 1 to perimeter

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            perimeter = 0
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in visited:
                        continue
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                    else:
                        perimeter += 1

            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return bfs(r, c)