import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # need heap to get two heaviest stones
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x - y)
        return 0 if len(max_heap) == 0 else abs(heapq.heappop(max_heap))
