class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetterCounts = {}

        for char in s:
            sLetterCounts[char] = 1 + sLetterCounts.get(char, 0)

        tLetterCounts = {}
        for char in t:
            tLetterCounts[char] = 1 + tLetterCounts.get(char, 0)
        
        return sLetterCounts == tLetterCounts