class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 or 2 steps at a time
        # to get to step n, we can either do:
            # (step n - 2) + 2
            # (step n - 1) + 1
            # two ways
        
        # tabulation - exhaustive, bottom up, iterative
        # memoization - non exaustive (only compute what you need), top down, recursive (call stack costs)
        one, two = 1, 1

        for i in range(n - 1):
            temp = one + two
            two = one
            one = temp
        
        return one


