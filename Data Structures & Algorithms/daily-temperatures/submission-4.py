class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to track days. a warmer day can be warmer for
        # several days. store index w/ temp for each day
        
        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prevDay, prevTemp = stack.pop()
                res[prevDay] = i - prevDay
            stack.append((i, temp))

        return res
            
