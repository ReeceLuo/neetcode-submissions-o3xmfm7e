class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        maxLength = 0
        l = 0
        r = 0

        mostFreq = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            mostFreq = max(mostFreq, count[s[r]])

            while r - l + 1 - mostFreq > k:
                count[s[l]] -= 1
                l += 1

            r += 1
            maxLength = max(maxLength, r - l)

        return maxLength

