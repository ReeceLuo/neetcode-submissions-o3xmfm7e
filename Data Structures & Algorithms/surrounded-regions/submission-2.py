from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        groups = []
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visited:
                    group = []
                    q = deque([(r, c)])
                    visited.add((r, c))

                    while q:
                        row, col = q.popleft()
                        group.append((row, col))

                        for dr, dc in DIRECTIONS:
                            nr, nc = row + dr, col + dc
                            if (0 <= nr < ROWS and
                                0 <= nc < COLS and
                                (nr, nc) not in visited and
                                board[nr][nc] == 'O'):
                                visited.add((nr, nc))
                                q.append((nr, nc))

                    groups.append(group)

        for group in groups:
            surrounded = True
            for r, c in group:
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    surrounded = False
                    break

            if surrounded:
                for r, c in group:
                    board[r][c] = 'X'