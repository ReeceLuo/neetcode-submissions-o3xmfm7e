from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # initial thought - use graph traversal to get groups of Os,
        # then check surroundings for all points in the group
            # group formation: O(m x n)
            # 

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()
        def get_groups(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            group = []
            while q:
                r, c = q.popleft()
                group.append((r, c))
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        board[nr][nc] == "O"):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
            return group
                

        groups = []
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    groups.append(get_groups(r, c))


        for group in groups:
            border = False
            for r, c in group:
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS):
                        border = True
                        break
            if not border:
                for r, c in group:
                    board[r][c] = "X"
            
        






        