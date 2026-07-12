class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sort ascending
        # start making groups

        if len(hand) % groupSize != 0:
            return False
        
        counts = {}
        for num in hand:
            counts[num] = counts.get(num, 0) + 1
        
        for i in range(int(len(hand) / groupSize)):
            start = None
            for num, count in counts.items():
                if count != 0:
                    start = num
                    break
            
            while (start - 1) in counts and counts[start - 1] != 0:
                start -= 1
            
            for j in range(groupSize):
                if (start + j) not in counts or counts[start + j] == 0:
                    return False
                counts[start + j] -= 1
        
        return True
            


