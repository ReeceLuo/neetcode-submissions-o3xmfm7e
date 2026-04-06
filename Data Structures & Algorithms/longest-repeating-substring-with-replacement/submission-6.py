class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        chars = {} # keep track of counts, which is most freq

        length = 0
        p1 = 0
        p2 = 0

        mostFreq = 0
        while p2 < len(s):
            chars[s[p2]] = chars.get(s[p2], 0) + 1
            mostFreq = max(mostFreq, chars[s[p2]])

            while p2 - p1 + 1 - mostFreq > k:
                chars[s[p1]] -= 1
                p1 += 1

            p2 += 1      
            length = max(length, p2 - p1)
      

        return length


