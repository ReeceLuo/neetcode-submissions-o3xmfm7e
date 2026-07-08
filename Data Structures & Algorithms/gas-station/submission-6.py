class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # two pointer approach: start at end, end at 0
            # slide end forward when car is able to
            # if tank is negative, slide start backward to see if
            # any prior sequence could make trip possible (positive)
        # when two pointers meet, it is circle

        start = len(gas) - 1
        end = 0
        tank = gas[start] - cost[start]

        while start > end: # while they don't meet
            if tank >= 0: # we WERE able to cover prev cost and make trip
                tank += gas[end] - cost[end]
                end += 1
            else: # cost > tank -> see if backtracking start can counteract
                start -= 1
                tank += gas[start] - cost[start]
        
        return start if tank >= 0 else -1