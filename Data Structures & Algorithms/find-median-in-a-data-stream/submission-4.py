# find median from data stream
# brute force - sort every on every insert O(m nlogn)

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums) % 2 == 0:
            x = self.nums[(len(self.nums) // 2) - 1]
            y = self.nums[len(self.nums) // 2]
            return (x + y) / 2
        else:
            return self.nums[len(self.nums) // 2]
        