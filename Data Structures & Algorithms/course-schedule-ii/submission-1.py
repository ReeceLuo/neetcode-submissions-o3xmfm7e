from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use kahn's algorithm to find topological sort

        adjacency_list = [[] for i in range(numCourses)]
        in_degrees = [0] * numCourses

        for course, prereq in prerequisites:
            in_degrees[course] += 1
            adjacency_list[prereq].append(course)

        q = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for neighbor in adjacency_list[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == numCourses else []



