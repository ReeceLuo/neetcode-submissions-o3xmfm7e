import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST for all points
        
        minCost = 0
        visited = set()
        minHeap = [(0, (points[0][0], points[0][1]))]

        while minHeap and len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            visited.add(point)
            minCost += cost
            for other in points:
                if (other[0], other[1]) in visited:
                    continue
                mDistance = abs(point[0] - other[0]) + abs(point[1] - other[1])
                heapq.heappush(minHeap, (mDistance, (other[0], other[1])))
        return minCost

