class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals overlap when one that started earlier
        # ends after another

        intervals.sort(key = lambda interval: interval[0])
        res = []

        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res