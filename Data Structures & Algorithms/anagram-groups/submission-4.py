class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # must check letter counts with others
        # brute force - check letter counts with first word
        # of each group, append to list if same, make new list if diff

        # dicts cant be keys, but tuples can
        
        seen = {}

        for word in strs:
            letterCounts = [0] * 26
            for letter in word:
                letterCounts[ord(letter) - ord('a')] += 1
            
            letterCounts = tuple(letterCounts)
            if letterCounts in seen:
                seen[letterCounts].append(word)
            else:
                seen[letterCounts] = [word]
        
        return list(seen.values())