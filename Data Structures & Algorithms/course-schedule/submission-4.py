class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return true when there is a valid topological sort (it is
        # a DAG). If not a DAG, there is a cycle, so not possible.
        # Used kahns algorithm

        # adjacency list for graph 
        # each vertex at an index
        adjacency_list = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for course, prereq in prerequisites:
            adjacency_list[prereq].append(course)
            in_degrees[course] += 1
        
        q = deque()
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                q.append(i)

        completed = 0
        while q:
            course = q.popleft()
            completed += 1
            for neighbor in adjacency_list[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)


        return completed == numCourses


