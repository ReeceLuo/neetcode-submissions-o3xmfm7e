class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1])
        remove = 0

        recent = None
        for interval in intervals:
            if recent and recent > interval[0]:
                remove += 1
            else:
                recent = interval[1]

        return remove



