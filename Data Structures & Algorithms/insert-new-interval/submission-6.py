class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # given sorted list of non overlapping intervals
        # we can iterate through intervals to see where to place new one
        # three cases:
            # 1. new interval ends before current starts, so we can
            # add and return it
            # 2. new interval starts after current ends, so we can move
            # on to the next
            # 3. if either 1 and 2 are untrue, then there is overlap.
        
        res = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else: # overlap
                start = min(newInterval[0], interval[0])
                end = max(newInterval[1], interval[1])
                newInterval = [start, end]
        
        res.append(newInterval)
        return res