class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0

        l = 0
        r = 0

        letters = set()
        while r < len(s):
            
            while s[r] in letters:
                letters.remove(s[l])
                l += 1

            letters.add(s[r])
            r += 1
            maxLength = max(maxLength, r - l)

        return maxLength