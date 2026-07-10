class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sort ascending
        # start making groups

        if len(hand) % groupSize != 0:
            return False

        counts = {}
        for num in hand:
            counts[num] = counts.get(num, 0) + 1
        
        hand.sort()
        for i in range(int(len(hand) / groupSize)):
            start = None
            for num in hand:
                if counts[num] != 0:
                    start = num
                    break

            for i in range(groupSize):
                if (start + i) not in counts or counts[start + i] == 0:
                    return False
                counts[start + i] -= 1
        
        return True

