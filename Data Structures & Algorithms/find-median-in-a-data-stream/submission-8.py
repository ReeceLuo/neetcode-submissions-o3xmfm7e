# find median of a list of integers
# brute force - sort each time and find middle value
# O(nlogn) for each findMedian call
    # for n calls, O(n^2logn)

# better - A median is just the middle value
    # average of: largest of lower half, smallest of upper half
    # to get these values, use maxheap for lower and minheap for upper

import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeapLower = []
        self.minHeapUpper = []

    def addNum(self, num: int) -> None:
        if self.minHeapUpper and num > self.minHeapUpper[0]:
            heapq.heappush(self.minHeapUpper, num)
        else:
            heapq.heappush(self.maxHeapLower, -(num))
        
        if len(self.minHeapUpper) > len(self.maxHeapLower) + 1:
            heapq.heappush(self.maxHeapLower, -(heapq.heappop(self.minHeapUpper)))
        elif len(self.maxHeapLower) > len(self.minHeapUpper) + 1:
            heapq.heappush(self.minHeapUpper, -(heapq.heappop(self.maxHeapLower)))

    def findMedian(self) -> float:
        if len(self.maxHeapLower) == len(self.minHeapUpper):
            return (-(self.maxHeapLower[0]) + self.minHeapUpper[0]) / 2
        if len(self.maxHeapLower) > len(self.minHeapUpper):
            return -(self.maxHeapLower[0])
        else:
            return self.minHeapUpper[0]







