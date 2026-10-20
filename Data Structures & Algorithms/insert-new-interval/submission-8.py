class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # sorted in ascending order by start time
        # add a new interval, merge any overlapping ones
        # note: overlapping = common point

        # 1. newInterval starts after current ends -> continue
        # 2. newInterval ends before current starts -> append + return
        # 3. overlap between -> merge
            # update newInterval: min(start times), max(endtimes)
            # continue

        res = []

        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        res.append(newInterval)
        return res



