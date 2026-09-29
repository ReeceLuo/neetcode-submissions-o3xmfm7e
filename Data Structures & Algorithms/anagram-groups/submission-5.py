class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams together
        # must check counts of each string
        # brute force: get counts of each string and first string
        # of each group, append if anagram, make new list if not

        # better - use hashmap

        letterCounts = {}

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            
            key = tuple(counts)
            if key not in letterCounts:
                letterCounts[key] = []

            letterCounts[key].append(word)
        
        res = []
        for key, value in letterCounts.items():
            res.append(value)

        return res