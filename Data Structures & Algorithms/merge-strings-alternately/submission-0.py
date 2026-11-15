class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0

        res = ""
        while p1 < len(word1) and p2 < len(word2):
            res += word1[p1]
            res += word2[p2]
            p1 += 1
            p2 += 1
        
        if p1 >= len(word1):
            res += word2[p2:]
        else:
            res += word1[p1:]

        return res