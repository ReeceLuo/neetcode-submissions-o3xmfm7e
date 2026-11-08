import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # count all letters, then use a maxheap to always add the most frequent letter
        # if prev = new, then return ""

        counts = defaultdict(int)
        for char in s:
            counts[char] += 1

        maxHeap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(maxHeap)

        prev = None
        coolDown = None
        output = ""
        while maxHeap or coolDown:
            if not maxHeap:
                heapq.heappush(maxHeap, coolDown)
                coolDown = None
            count, char = heapq.heappop(maxHeap)
            if char == prev: # chars are touching
                return ""
            output += char
            prev = char
            if coolDown:
                heapq.heappush(maxHeap, coolDown)
                coolDown = None
            if count + 1 == 0:
                continue
            coolDown = (count + 1, char)

        return output





