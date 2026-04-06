class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}

        length = 0
        
        p1 = 0
        p2 = 0

        mostFreq = 0
        while p2 < len(s):
            # Add character to dict
            chars[s[p2]] = 1 + chars.get(s[p2], 0)
            mostFreq = max(mostFreq, chars[s[p2]])
            # Ensure the window is valid
            while p2 - p1 + 1 - mostFreq > k:
                chars[s[p1]] -= 1
                p1 += 1

            # Update length (if valid)
            length = max(p2 - p1 + 1, length)

            p2 += 1

        return length
