import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force - sort, index at k
        # option: maxheap and pop k times
            # O(n + klogn), O(n) space
        # option: minheap of size k
            # O(k + nlogk), O(k) space

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

        