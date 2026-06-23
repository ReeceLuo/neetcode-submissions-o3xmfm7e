import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # largest square gives greatest distance
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, x, y))
        
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res