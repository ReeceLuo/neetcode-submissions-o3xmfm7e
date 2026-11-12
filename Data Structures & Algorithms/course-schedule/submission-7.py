class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # must take b before a
        # use kahns algorithm
        # build adj list

        adj_list = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degrees[course] += 1
        
        q = deque()
        for i, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(i)
        
        processed = 0
        while q:
            course = q.popleft()
            processed += 1
            for neighbor in adj_list[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)

        return processed == numCourses





