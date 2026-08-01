class Solution:
    def climbStairs(self, n: int) -> int:
        # step(n) equals step(n - 1) + 1 or step(n - 2) + 2,
        # so step(n) has step(n - 1) + step(n - 2) ways

        # subproblems are recomputed, so we can store them
        # observation: using tabulation (bottom up), we
        # are not even using subproblems again after we calculate
        # the next one. We can space optimize this

        table = [-1] * n

        def dfs(i):
            if i == n:
                return 1
            if i > n:       # stop exploring, have passed n steps
                return 0
            if table[i] == -1:
                table[i] = dfs(i + 1) + dfs(i + 2)
            return table[i]

        return dfs(0)


