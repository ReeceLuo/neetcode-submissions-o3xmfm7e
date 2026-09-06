class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # get length of longest substring that contains
        # one distinct character
        # take character that has appears most frequently
        # while the most substring length - most frequent > k, 
        # shrink the substring
        
        counts = {}
        mostFreq = 0
        maxLen = 0

        l, r = 0, 0

        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1
            mostFreq = max(mostFreq, counts[s[r]])
            r += 1
            while r - l - mostFreq > k:
                counts[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l)
        
        return maxLen
