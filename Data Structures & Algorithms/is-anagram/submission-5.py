class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = {}
        for char in s:
            sCounts[char] = sCounts.get(char, 0) + 1
        
        tCounts = {}
        for char in t:
            tCounts[char] = tCounts.get(char, 0) + 1
        
        return sCounts == tCounts