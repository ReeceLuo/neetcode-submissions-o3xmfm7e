class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if (not stack or
                stack[-1] < 0 or
                asteroid > 0):
                stack.append(asteroid)
                continue
            
            destroyed = False
            while stack and stack[-1] > 0:
                if stack[-1] > abs(asteroid):
                    destroyed = True
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    destroyed = True
                    break
            if not destroyed:
                stack.append(asteroid)

        return stack
