class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0

        l = 0
        r = 0

        ltrSet = set()
        while r < len(s):
            
            while s[r] in ltrSet:
                ltrSet.remove(s[l])
                l += 1
  
            maxLength = max(maxLength, r - l + 1)
            ltrSet.add(s[r])
            r += 1

        return maxLength