import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # build adjacency list of the graph O(V + E) time
        
        # starting at node k
        # add all the node's edge weights to the heap
        # pop the smallest and start processing again

        # each value 

        adj_list = [[] for _ in range(n + 1)]

        for u, v, t in times:
            adj_list[u].append((v, t))
        
        heap = [(0, k)] # stores edge times
        
        seen = set()
        curr = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            curr = time

            for target, time in adj_list[node]:
                if target not in seen:
                    heapq.heappush(heap, (curr + time, target))
        
        return curr if len(seen) == n else -1






