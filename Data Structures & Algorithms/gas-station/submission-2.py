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

        total = 0
        travelled = 0
        i = 0
        start = 0
        visited = set()
        while travelled < len(gas):
            if i == len(gas):
                i = 0
            total += gas[i]
            total -= cost[i]
            i += 1
            travelled += 1
            if total < 0:
                start = i
                if start in visited:
                    return -1
                visited.add(start)
                total = 0
                travelled = 0

        return start
            