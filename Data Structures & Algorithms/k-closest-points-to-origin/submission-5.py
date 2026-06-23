import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # largest square gives greatest distance
        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:k]
