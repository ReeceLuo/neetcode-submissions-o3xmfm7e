# find median from data stream
# brute force - sort every on every insert 
    # O(m nlogn) for n numbers and m adds

# better - use two heaps: maxheap for lower half, minheap for upper half
    # median is middle of a sorted array - simulate by finding largest
    # of lower half and smallest of upper half to get middle values

    # keep one heap larger than the other. (we will choose lower)
    # if odd # of nums, median is top value on larger heap
    # if even # of nums, median average of two heap tops

    # O(log n) median finds

    # also must check top of heaps to see which to put in

import heapq

class MedianFinder:

    def __init__(self):
        self.lower = [] # maxHeap
        self.upper = [] # minHeap

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -(num))
        
        if len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -(heapq.heappop(self.upper)))
        elif len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -(heapq.heappop(self.lower)))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -(self.lower[0])
        if len(self.lower) < len(self.upper):
            return self.upper[0]
        return (-(self.lower[0]) + self.upper[0]) / 2
    
    # lower: [-1, -2]
    # upper: [3]
        