class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return result where each val is num days until warmer day

        # brute force - for each day, scan until warmer day - O(n^2)

        # observation - a day could be warmer for multiple days
        # keep track of days on a stack
        res = [0] * len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prevTemp, j = stack.pop()
                res[j] = i - j

            stack.append((temp, i))

        return res

        # [(40, 5), (28, 6)]

        # [1, 4, 1, 2, 1, 0, 0]

