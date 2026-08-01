class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, either take 1 or 2 steps at a time
        # take current cost and min cost of path from 1 step or 2 step,
        # calling recursively

        cache = [-1] * len(cost)
        
        def dfs(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]
        
        return min(dfs(0), dfs(1))
            