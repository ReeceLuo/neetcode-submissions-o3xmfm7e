class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # level order traversal

        adj_list = defaultdict(list)
        for a, b, p in flights:
            adj_list[a].append((b, p))

        q = deque()
        q.append((src, 0))
        dist = [float("inf")] * n
        for i in range(k + 1):
            newDist = dist.copy()

            for i in range(len(q)):
                node, price = q.popleft()
                for neighbor, p in adj_list[node]:

                    if price + p < newDist[neighbor]:
                        q.append((neighbor, price + p))
                        newDist[neighbor] = price + p

            dist = newDist
        
        return dist[dst] if dist[dst] != float("inf") else -1

