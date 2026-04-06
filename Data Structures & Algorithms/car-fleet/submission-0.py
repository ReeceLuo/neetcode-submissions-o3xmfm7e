class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force: until every element has not reached target,
        # keep iterating over position while adding speed values

        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)

        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)