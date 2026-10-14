class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return k closest points to origin
        # distance = sqrt(x^2 + y^2)

        # sort points by x^2 + y^2
        # slice to get [:k]

        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:k]