import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # build adjacency list of the graph O(V + E) time
        
        # starting at node k
        # add all the node's edge weights to the heap
        # pop the smallest and start processing again

        # by the time 

        adj_list = [[] for i in range(n + 1)]

        for src, target, time in times:
            adj_list[src].append((target, time))

        heap = []
        heap.append((0, k))
        visited = set()
        curr = 0

        while heap:
            time, src = heapq.heappop(heap)
            if src in visited:
                continue
            curr = time
            visited.add(src)

            for target, time in adj_list[src]:
                if target not in visited:
                    heapq.heappush(heap, (curr + time, target))
        
        return curr if len(visited) == n else -1



