import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elements within the array
        
        # must scan all elements
        # can use heap

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # buckets store numbers using index as their counts
        # max count is len(nums)
        buckets = [[] for _ in range(len(nums))]
        for key, value in counts.items():
            buckets[value - 1].append(key)

        res = []
        while buckets and len(res) < k:
            bucket = buckets.pop()
            while bucket and len(res) < k:
                res.append(bucket.pop())

        return res