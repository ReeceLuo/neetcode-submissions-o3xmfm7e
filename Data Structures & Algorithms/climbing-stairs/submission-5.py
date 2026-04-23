class Solution:
    def climbStairs(self, n: int) -> int:
        # step(n) equals step(n - 1) + 1 or step(n - 2) + 2,
        # so step(n) has step(n - 1) + step(n - 2) ways

        # subproblems are recomputed, so we can store them
        # observation: using tabulation (bottom up), we
        # are not even using subproblems again after we calculate
        # the next one. We can space optimize this

        if n == 1:
            return 1

        prev = 1
        curr = 2

        for i in range(2, n):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr


