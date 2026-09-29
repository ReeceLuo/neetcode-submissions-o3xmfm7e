import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elements within the array
        
        # must scan all elements
        # can use heap

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for key, value in counts.items():
            heap.append((-(value), key))
        
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            count, num = heapq.heappop(heap)
            res.append(num)

        return res