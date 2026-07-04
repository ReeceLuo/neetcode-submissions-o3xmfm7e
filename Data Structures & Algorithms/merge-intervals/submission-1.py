class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by starting times. if end time of most recent
        # interval is >= starting time of current, merge them
        # merge: take largest end time of the two
            # (current interval could be entirely within previous)

        intervals.sort(key = lambda interval: interval[0])

        res = []
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                # merge
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res



