class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 or 2 steps at a time
        # to get to step n, we can either do:
            # (step n - 2) + 2
            # (step n - 1) + 1
            # two ways
        
        # tabulation - exhaustive, bottom up, iterative
        # memoization - non exaustive (only compute what you need), top down, recursive (call stack costs)
        if n < 2:
            return 1

        table = [-1] * n
        table[0] = 1
        table[1] = 2

        for i in range(2, n):
            if table[i] == -1:
                table[i] = table[i - 2] + table[i - 1]
        
        return table[n - 1]