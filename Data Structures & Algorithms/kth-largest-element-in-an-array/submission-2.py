import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting - O(nlogn)
        # use minheap size of k - as we build heap, pop elements
        # element at root will be kth largest (all below will be larger,
        # all popped will be lower)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
