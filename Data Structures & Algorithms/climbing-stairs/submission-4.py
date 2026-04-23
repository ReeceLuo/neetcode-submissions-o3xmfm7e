class Solution:
    def climbStairs(self, n: int) -> int:
        # step(n) equals step(n - 1) + 1 or step(n - 2) + 2,
        # so step(n) has step(n - 1) + step(n - 2) ways

        # subproblems are recomputed, so we can store them

        if n == 1:
            return 1

        table = [-1] * n
        # base cases
        table[0] = 1
        table[1] = 2

        for i in range(2, n):
            table[i] = table[i - 1] + table[i - 2]

        return table[n - 1]