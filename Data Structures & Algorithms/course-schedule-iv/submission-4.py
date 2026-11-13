from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build out adj_list of each course and its prereqs,
            # use a set to store courses
        # do dfs for each

        adj_list = [set() for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj_list[prereq].add(course)
            in_degrees[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)

        # options: 
        # 1. for each course, store the courses it is a prereq for  
            # if we do this, we will need to do a dfs to the course
            # as we are only storing prereqs one degree away (direct, no
            # indirect prereqs)
        # 2. for each course, store its prereqs

        while q:
            course = q.popleft()
            isPrereq[course].add(course)
            for neighbor in adj_list[course]:
                isPrereq[neighbor] |= isPrereq[course]
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)

        res = []
        for u, v in queries:
            # check if u is prereq for v
            res.append(u in isPrereq[v])

        return res










