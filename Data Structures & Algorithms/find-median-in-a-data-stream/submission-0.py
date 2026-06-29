import heapq

class MedianFinder:
    # in a live data stream, use heaps to keep track of median
    # maxheap of smaller, minheap of larger
    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -(num))
        
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -(heapq.heappop(self.lower)))
        elif len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -(heapq.heappop(self.upper)))

    def findMedian(self) -> float:
        if len(self.upper) == len(self.lower):
            return (self.upper[0] + -(self.lower[0])) / 2
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        return -(self.lower[0])

        