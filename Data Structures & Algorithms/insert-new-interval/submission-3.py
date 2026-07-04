class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals is sorted in ascending order
        # insert new interval while maintaining sorted property
            # merge intervals if overlapping

        allIntervals = []
        for interval in intervals:
            if newInterval[0] < interval[0]:
                allIntervals.append(newInterval)
            allIntervals.append(interval)
        
        if len(allIntervals) == len(intervals):
            allIntervals.append(newInterval)

        # [[1,2],[3,5],[4, 8],[6,7],[8,10],[12,16]]
        res = []
        for interval in allIntervals:
            # if latest end time >= start time, merge
            if res and res[-1][1] >= interval[0]:
                if interval[1] > res[-1][1]:
                    res[-1][1] = interval[1]
            else:
                res.append(interval)

        return res