class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        
        for i in range(n):
            cache[0][i] = 1
        
        for i in range(m):
            cache[i][0] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                cache[r][c] = cache[r - 1][c] + cache[r][c - 1]

        return cache[m - 1][n - 1]
