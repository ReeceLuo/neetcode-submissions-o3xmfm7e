import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance from origin is sqrt(x^2 + y^2)
        # we know the largest x^2 + y^2 value will result in the largest distance, so we don't NEED the sqrt()

        points.sort(key = lambda point: (point[0]**2 + point[1]**2)**(1/2))
        return points[:k]