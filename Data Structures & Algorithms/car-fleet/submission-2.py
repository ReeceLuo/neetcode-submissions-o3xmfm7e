class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force: until every element has not reached target,
        # keep iterating over position while adding speed values

        # Cars cannot pass one another, so if a faster car catches
        # up to a car in front of it, they are limited by the speed of
        # car in front
        # This means we can sort by position

        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)