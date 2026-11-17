"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # edge cases: empty intervals
        # no overlap, full overlap

        intervals.sort(key = lambda x: x.start)

        prev = None
        for interval in intervals:
            if prev and prev.end > interval.start:
                return False
            prev = interval
        
        return True


