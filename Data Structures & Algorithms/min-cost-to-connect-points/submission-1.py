import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST problem - connect all points
        # use heap to continuously get smallest edge until
        # all points added
        minCost = 0
        visited = set()
        heap = [(0, points[0][0], points[0][1])]
        while heap and len(visited) < len(points):
            cost, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            minCost += cost
            visited.add((x, y))
            for p in points:
                if (p[0], p[1]) in visited:
                    continue
                dist = abs(x - p[0]) + abs(y - p[1])
                heapq.heappush(heap, (dist, p[0], p[1]))
        
        return minCost
