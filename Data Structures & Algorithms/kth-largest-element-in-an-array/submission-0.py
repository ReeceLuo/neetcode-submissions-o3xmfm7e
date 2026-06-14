import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting + iterating: O(nlogn) runtime, O(1) space
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = -1
        for i in range(k - 1):
            heapq.heappop(nums)
        return -(heapq.heappop(nums))