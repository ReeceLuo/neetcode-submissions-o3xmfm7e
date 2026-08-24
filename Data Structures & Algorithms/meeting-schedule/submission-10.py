"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # given intervals, determine if there is conflict
        intervals.sort(key = lambda x: x.start)
        if not intervals:
            return True

        prevEnd = intervals[0].end

        for i in range(1, len(intervals)):
            start, newEnd = intervals[i].start, intervals[i].end
            if start < prevEnd:
                return False
            prevEnd = newEnd
        
        return True
