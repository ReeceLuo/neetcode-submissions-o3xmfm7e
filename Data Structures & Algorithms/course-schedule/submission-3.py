class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return true when there is a valid topological sort (it is
        # a DAG). If not a DAG, there is a cycle, so not possible.
        # Used khans algorithm

        # adjacency list for graph 
        # each vertex at an index
        adjacency_list = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses    # track in-degree of each vertex

        for course, prereq in prerequisites:
            in_degree[course] += 1
            adjacency_list[prereq].append(course)
        
        # add vertices with 0 in degree to queue
        # (only have outgoing edges, so must be start of topological ordering)
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        finished_courses = 0
        while q:
            course = q.popleft()    # process / complete course
            finished_courses += 1
            for neighbor in adjacency_list[course]:
                in_degree[neighbor] -= 1
                # substructure, like working with smaller DAG
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return finished_courses == numCourses

