import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance from origin is sqrt(x^2 + y^2)
        # we know the largest x^2 + y^2 value will result in the largest distance, so we don't NEED the sqrt()

        heap = []
        for p in points:
            heapq.heappush(heap, (-(p[0]**2 + p[1]**2), p))
            if len(heap) > k:
                heapq.heappop(heap)

        return [p for dist, p in heap]


