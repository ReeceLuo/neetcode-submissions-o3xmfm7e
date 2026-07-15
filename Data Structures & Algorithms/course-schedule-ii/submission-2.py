from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        q = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        # 0, 2

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return res if len(res) == numCourses else []


