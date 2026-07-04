class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals is sorted in ascending order
        # insert new interval while maintaining sorted property
            # merge intervals if overlapping
        # use greedy approach

        res = []
        for i in range(len(intervals)):
            # new interval ends before interval starts
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                continue
            else: # overlap
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end]
            
        res.append(newInterval)
        return res