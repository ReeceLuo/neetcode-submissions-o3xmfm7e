class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological ordering of a DAG
        # topsort - do dfs and add vertices to front of ordering
        # based on processing time

        # essentially given a list of edges, is it a DAG
        
        # implementation - adjacency list

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting: # there is a cycle
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

