class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # think about greedy choice / if it leads to optimal solution
        # ideas:
            # start (gas - cost of next location) is smallest
            # start just past largest cost???
            # where can we choose to

        # keep track of running total - if ever negative, reset
        # we know this is the method to use because the sequence of numbers
        # dictates if we can go or not. We are trying to find if we
        # can go across the entire sequence, so just finding the place
        # that has the greatest (gas - cost) value is not logically correct.
        # similar idea to subarray max

        n = len(gas)
        start, end = n - 1, 0
        tank = gas[start] - cost[start]
        while start > end:
            if tank < 0:
                start -= 1      # shift left
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1
        
        return start if tank >= 0 else -1
