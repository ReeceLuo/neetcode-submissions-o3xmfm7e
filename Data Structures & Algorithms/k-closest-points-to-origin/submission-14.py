class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return k closest points to origin
        # distance = sqrt(x^2 + y^2)

        # 1.
        # sort points by x^2 + y^2
        # slice to get [:k]
        # O(nlogn)

        #2.
        # use minheap of size n, pop k times
        # O(n) heapify + O(klogn) comparisons
        # O(n) space

        #3.
        # use maxheap of size k
        # O(nlogk) comparisons
        # O(k) space
        heap = []
        for p in points:
            heapq.heappush(heap, (-(p[0]**2 + p[1]**2), p))
            if len(heap) > k:
                heapq.heappop(heap)

        return [p for dist, p in heap]



