class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # while no duplicate, continue expanding substring
        # if there is duplicate, shrink until no more

        l, r = 0, 0
        chars = set()
        maxLen = 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            r += 1
            maxLen = max(maxLen, r - l)
        
        return maxLen

