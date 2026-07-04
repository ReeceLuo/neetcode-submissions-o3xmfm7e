class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # take the interval that has earliest end time to avoid overlapping
        
        remove = 0
        
        intervals.sort(key = lambda interval: interval[0])
        recent = None
        for interval in intervals:
            if recent and recent[1] > interval[0]:
                recent[1] = min(recent[1], interval[1])
                remove += 1
            else:
                recent = interval
        
        return remove