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
        for i in range(len(buckets) -1, -1, -1):
            if len(res) >= k:
                break
            if not buckets[i]:
                continue
            while buckets[i] and len(res) < k:
                res.append(buckets[i].pop())

        return res
