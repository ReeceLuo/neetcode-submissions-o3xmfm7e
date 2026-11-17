
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # no adjacent characters are the same
        # try using most frequent characters when possible
            # get with max heap
        
        # count occurrences of each char
        # add to heap
        # keep track of letter on cooldown
        
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        
        heap = [(-(count), char) for char, count in counts.items()]
        heapq.heapify(heap)
        res = []

        coolDown = None
        while heap or coolDown:
            if not heap:
                return ""

            count, char = heapq.heappop(heap)
            res.append(char)
            if coolDown:
                heapq.heappush(heap, coolDown)
                coolDown = None
            count += 1
            if count:
                coolDown = (count, char)

        return "".join(res)

        # abbccdd
        # b, c, d, a, b, c, d
        # cooldown: 












