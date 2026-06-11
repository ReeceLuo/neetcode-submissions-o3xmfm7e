import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        vals = set()
        points_hm = {}

        for x, y in points:
            dist = x**2 + y**2
            if dist not in vals:
                distances.append(dist)
                vals.add(dist)
            if dist in points_hm:
                points_hm[dist].append([x, y])
                continue
            points_hm[dist] = [[x, y]]
        
        res = []
        heapq.heapify(distances)
        while len(res) < k:
            dist = heapq.heappop(distances)
            if dist in points_hm:
                for point in points_hm[dist]:
                    res.append(point)
                    if len(res) >= k:
                        break
        
        return res


            




