import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # get min cost to connect all points together
        # MST - tree w/ minimum weight that spans all points
        # for each point, compute distance to other points

        # adj_list = defaultdict(list)
        # for i, x, y in enumerate(points):
        #     for j, a, b in enumerate(points):
        #         if j == i:
        #             continue
        #         adj_list[(x, y)].append((abs(x - a) + abs(y - b), (a, b)))
        total = 0
        heap = [(0, points[0][0], points[0][1])]
        visited = set()
        while heap:
            dist, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            total += dist
            visited.add((x, y))
            for a, b in points:
                if (a, b) in visited:
                    continue
                heapq.heappush(heap, (abs(x - a) + abs(y - b), a, b))

        return total


