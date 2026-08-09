import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph - adj list

        # dijkstras

        adj_list = [[] for _ in range(n + 1)]

        for src, target, time in times:
            adj_list[src].append((target, time))
        
        heap = [(0, k)]
        seen = set()

        time = 0
        while heap and len(seen) < n:
            currTime, currNode = heapq.heappop(heap)
            if currNode in seen:
                continue
            time = currTime
            seen.add(currNode)
            for target, t in adj_list[currNode]:
                if target not in seen:
                    heapq.heappush(heap, (time + t, target))

        return time if len(seen) == n else -1

