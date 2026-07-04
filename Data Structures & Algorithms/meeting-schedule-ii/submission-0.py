"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by starting times and iterate across
        # maintain min heap of end times. when an interval is run
        # add its end time to heap. this gives earliest end time
        # so that it can be removed if room is free

        heap = []
        intervals.sort(key = lambda interval: interval.start)

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        
        return len(heap)

