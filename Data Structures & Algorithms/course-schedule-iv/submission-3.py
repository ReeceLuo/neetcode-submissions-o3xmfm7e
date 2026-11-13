from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build out adj_list of each course and its prereqs,
            # use a set to store courses
        # do dfs for each

        adj_list = defaultdict(list)

        for prereq, course in prerequisites:
            adj_list[course].append(prereq)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj_list[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        
        return res

