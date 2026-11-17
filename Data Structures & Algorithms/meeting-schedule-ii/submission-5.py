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
        # same time is not overlap

        # sort by start time
        # use minHeap to track end times
            # for next iterations, check earliest end times. if 
            # our current start time is after earliest end time, we can 
            # replace it. if not, we have to push current time onto stack
        
        intervals.sort(key = lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap)




