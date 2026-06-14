import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting + iterating: O(nlogn) runtime, O(1) space
        # maxheap + popping: O(n) runtime, O(n) space
        # minheap of size k, build while iterating
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
