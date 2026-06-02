from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # best solution
        # start bfs from border O's, since any other O's that
        # are the same group as them cannot be surrounded
        # mark these groups, any remaining Os should be X

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            if board[r][c] != "O":
                return
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                board[r][c] = "NOT SURROUNDED"
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and
                        0 <= col < COLS and
                        board[row][col] == "O"):
                        q.append((row, col))

        # left/right
        for r in range(ROWS):
            bfs(r, 0)
            bfs(r, COLS - 1)
        # top/bottom
        for c in range(COLS):
            bfs(0, c)
            bfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "NOT SURROUNDED": # part of group that touches edge
                    board[r][c] = "O"
            



