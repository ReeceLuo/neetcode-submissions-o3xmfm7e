class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check if a string contains a permutation of another string
        # sliding window of length s1

        if len(s1) > len(s2):
            return False

        counts1 = {}
        for char in s1:
            counts1[char] = counts1.get(char, 0) + 1
        
        
        counts2 = {}
        for i in range(len(s1) - 1):
            counts2[s2[i]] = counts2.get(s2[i], 0) + 1

        l, r = 0, len(s1) - 1

        while r < len(s2):
            counts2[s2[r]] = counts2.get(s2[r], 0) + 1
            if counts1 == counts2:
                return True
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                counts2.pop(s2[l])
            r += 1
            l += 1
        return False

            
            




