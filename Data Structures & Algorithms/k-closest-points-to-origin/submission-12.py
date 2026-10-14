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

        heap = []
        for point in points:
            heap.append((point[0]**2 + point[1]**2, point))
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res

        #3.
        # use maxheap of size k
        # O(nlogk) comparisons
        # O(k) space



