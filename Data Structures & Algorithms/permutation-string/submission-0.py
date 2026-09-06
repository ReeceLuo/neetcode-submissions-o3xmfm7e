class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check if a string contains a permutation of another string

        counts1 = {}
        for char in s1:
            counts1[char] = counts1.get(char, 0) + 1
        
        l, r = 0, 0

        for i, char in enumerate(s2):
            if char in counts1:
                r = i
                counts2 = {}
                while r < len(s2):
                    counts2[s2[r]] = counts2.get(s2[r], 0) + 1
                    if counts2[s2[r]] > counts1.get(s2[r], 0):
                        break
                    if counts2 == counts1:
                        return True
                    r += 1

        return False
