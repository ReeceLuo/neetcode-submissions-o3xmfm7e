class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # must check letter counts with others
        # brute force - check letter counts with first word
        # of each group, append to list if same, make new list if diff

        # dicts cant be keys, but tuples can
        
        seen = {}

        for word in strs:
            charCounts = [0] * 26
            for char in word:
                charCounts[ord(char) - ord('a')] += 1
            key = tuple(charCounts)
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]

        return list(seen.values())