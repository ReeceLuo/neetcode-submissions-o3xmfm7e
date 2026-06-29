import heapq

class MedianFinder:

    def __init__(self):
        self.lower = []     # maxheap
        self.upper = []     # minheap

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
        if len(self.lower) == len(self.upper):
            return (-(self.lower[0]) + self.upper[0]) / 2
        if len(self.lower) > len(self.upper):
            return -(self.lower[0])
        return self.upper[0]




        