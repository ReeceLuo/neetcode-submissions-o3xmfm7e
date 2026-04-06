class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # must check letter counts with others
        # brute force - check letter counts with first word
        # of each group, append to list if same, make new list if diff

        # dicts cant be keys, but lists can

        anagrams = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return list(anagrams.values())