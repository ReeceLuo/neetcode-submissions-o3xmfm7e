import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each cycle allows completion of one task
        # idential tasks must be separted by n CPU cycles
        # use max heap, store tuples
        
        task_count = {}
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1
        
        maxHeap = []
        for task, count in task_count.items():
            maxHeap.append(-(count))
        
        time = 0
        heapq.heapify(maxHeap)
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]      # jump ahead
            else:
                count = heapq.heappop(maxHeap) # most frequent task
                if count + 1 != 0:
                    q.append([count + 1, time + n])     # time + n is time when
            if q and q[0][1] == time:
                count, time = q.popleft()
                heapq.heappush(maxHeap, count)
        
        return time


