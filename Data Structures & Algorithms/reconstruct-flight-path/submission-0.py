class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # make flight path using each ticket starting from JFK
        # give smallest one
        
        # Eulerian path - visits every edge (ticket) exactly once
        # must find smallest eulerian paht

        # Hierholzer's algorithm - finds eulerian paths/cycles by 
        # performing graph traversal, taking all available edges
        # until there are no more available outgoing edges
        # add current node to front of res and backtrack

        # adj_list = {}
        # for src, target in sorted(tickets)[::-1]:   # iterating backwards on sorted list
        #     if src not in adj_list:
        #         adj_list[src] = []
        #     adj_list[src].append(target)

        adj_list = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj_list[src].append(dst)

        res = []
        def dfs(src):
            while adj_list[src]:
                target = adj_list[src].pop()
                dfs(target)
            res.append(src)

        dfs('JFK')
        return res[::-1]

        

        
