class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals is sorted in ascending order
        # insert new interval while maintaining sorted property
            # merge intervals if overlapping
        # use greedy approach

        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        res.append(newInterval)
        return res