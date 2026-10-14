class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a task scheduler
        # need to count each task
        # 

        taskCount = {}
        for task in tasks:
            taskCount[task] = taskCount.get(task, 0) + 1

        heap = []
        for task, count in taskCount.items():
            heap.append((-(count), task))
        heapq.heapify(heap)

        # when a task is completed, it must be put on cooldown
        # use a queue to track which task is available and which is not
        
        q = deque()
        time = 0
        while heap or q:
            if not heap:
                time = q[0][0]
            if q and q[0][0] == time:
                time, task = q.popleft()
                heapq.heappush(heap, (-(taskCount[task]), task))

            count, task = heapq.heappop(heap)
            time += 1
            taskCount[task] -= 1
            if taskCount[task] == 0:
                continue
            q.append((time + n, task))

        return time
        

