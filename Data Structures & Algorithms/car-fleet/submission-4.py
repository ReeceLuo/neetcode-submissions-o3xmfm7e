class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # one lane, cars cannot pass
        # once car reaches car in front position, it drives at their speed
            # joins fleet

        # observation: cars can only go as fast as the leaders of their
        # fleets. use stack to track most recent fleet leader and if 
        # car will join by end of road.
            # if they will, then continue since they will join that fleet
            # if not, then they are a separate group that will be
            # potential leader for cars behind it

        posAndSpeed = []
        for i in range(len(position)):
            posAndSpeed.append((position[i], speed[i]))
        
        posAndSpeed.sort(reverse = True)

        stack = []

        for i in range(len(posAndSpeed)):
            pos, speed = posAndSpeed[i]
            time = (target - pos) / speed
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)

        # 1, 12