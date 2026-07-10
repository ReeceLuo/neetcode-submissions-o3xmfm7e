import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sort ascending
        # start making groups

        if len(hand) % groupSize != 0:
            return False

        counts = {}
        for num in hand:
            counts[num] = counts.get(num, 0) + 1

        nums = set(hand)
        for i in range(int(len(hand) / groupSize)):
            start = min(nums)
            for i in range(groupSize):
                if (start + i) not in counts:
                    return False
                counts[start + i] -= 1
                if counts[start + i] == 0:
                    del counts[start + i]
                    nums.remove(start + i)
            
        return True
        