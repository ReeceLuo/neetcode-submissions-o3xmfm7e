from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # initial thought - use graph traversal to get groups of Os,
        # then check surroundings for all points in the group
            # group formation: O(m x n)
            # checking each cell: O(m x n)
            # total aympt runtime: O(m x n)
            # space: O(m x n) each cell only processed once
        
        # better - do graph traversal for all edge cells, mark those
        # as not surrounded, then change all other Os to xs

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            board[r][c] = "T"
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        board[nr][nc] == "O"):
                        board[nr][nc] = "T"
                        q.append((nr, nc))
        
        for r in range(ROWS):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][COLS - 1] == "O":
                bfs(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == "O":
                bfs(0, c)
            if board[ROWS - 1][c] == "O":
                bfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"






