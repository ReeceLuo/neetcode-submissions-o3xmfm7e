class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # otherwise, some start index works
        # scan across and if tank is ever negative, we know we cannot
        # start at any previous index
        start = 0
        tank = 0
        for i in range(len(gas)):
            if tank < 0:
                start = i # start index must be after prev indices
                tank = 0  # reset tank
            tank += gas[i] - cost[i]

        return start
        