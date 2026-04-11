class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []

        # will have to keep a count
        # sort by frequency

        frequencies = [[] for _ in nums]

        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for key, value in seen.items():
            frequencies[value - 1].append(key)

        while len(output) < k:
            group = frequencies.pop()
            while group and len(output) < k:
                output.append(group.pop())

        return output