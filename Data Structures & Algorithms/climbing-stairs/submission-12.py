class Solution:
    def climbStairs(self, n: int) -> int:
        # step(n) equals step(n - 1) + 1 or step(n - 2) + 2,
        # so step(n) has step(n - 1) + step(n - 2) ways

        # subproblems are recomputed, so we can store them
        # observation: using tabulation (bottom up), we
        # are not even using subproblems again after we calculate
        # the next one. We can space optimize this

        if n < 2:
            return 1

        cache = [-1] * n
        cache[0] = 1
        cache[1] = 2

        for i in range(n):
            if cache[i] == -1:
                cache[i] = cache[i - 1] + cache[i - 2]
        
        return cache[n - 1]