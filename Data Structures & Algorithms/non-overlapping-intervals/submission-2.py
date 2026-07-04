class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # take the interval that has earliest end time to avoid overlapping
        
        remove = 0
        
        intervals.sort(key = lambda interval: interval[1])
        recent = None
        for start, end in intervals:
            if recent and recent > start:
                remove += 1
            else:
                recent = end
        return remove