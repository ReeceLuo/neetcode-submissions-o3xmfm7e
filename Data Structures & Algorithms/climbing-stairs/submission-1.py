class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        subproblems = [-1] * n
        subproblems[0] = 1
        subproblems[1] = 2

        def stairs(n: int):
            if subproblems[n - 1] == -1:
                subproblems[n - 1] = stairs(n - 1) + stairs(n - 2)
            return subproblems[n - 1]

        return stairs(n)