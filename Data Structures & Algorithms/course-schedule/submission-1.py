class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological ordering of a DAG
        # Khan's topsort - do dfs and add vertices to front of ordering
        # based on processing time

        # essentially given a list of edges, is it a DAG
        
        # implementation - adjacency list
        adjacency_list = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            indegree[course] += 1
            adjacency_list[prereq].append(course)
        
        # check for indegree of 0 and add to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)         # refer to vertex by its index

        num_finished = 0
        while q:
            vertex = q.popleft()
            num_finished += 1
            # finish a course, go to its 
            for neighbor in adjacency_list[vertex]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # if there are no courses with indegree of 0, then there is no
        # source vertex, meaning it is not a DAG (every vertex has another
        # pointing to it and thus there is a cycle)
        return num_finished == numCourses

        
