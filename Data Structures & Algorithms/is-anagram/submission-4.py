class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # strings are anagrams if they the same letter counts
        # have to count the characters

        sCount = {}
        for char in s:
            sCount[char] = sCount.get(char, 0) + 1
        
        tCount = {}
        for char in t:
            tCount[char] = tCount.get(char, 0) + 1

        return sCount == tCount