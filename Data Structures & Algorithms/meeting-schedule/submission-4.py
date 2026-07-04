"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)

        recent = None
        for interval in intervals:
            if recent and recent > interval.start:
                return False
            recent = interval.end
        return True