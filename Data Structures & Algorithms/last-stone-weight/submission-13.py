import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # take two heaviest stones - max heap
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) >= 2:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x == y:
                continue
            heapq.heappush(maxHeap, -(abs(x - y)))
        
        return -(maxHeap[0]) if len(maxHeap) > 0 else 0

        # [4,1]


