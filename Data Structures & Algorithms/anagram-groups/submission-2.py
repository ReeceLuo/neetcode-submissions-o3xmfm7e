class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # must check letter counts with others
        # brute force - check letter counts with first word
        # of each group, append to list if same, make new list if diff

        # dicts cant be keys, but lists can
        output = []

        for word in strs:
            currCounts = {}
            for char in word:
                currCounts[char] = currCounts.get(char, 0) + 1
            
            added = False
            for i in range(len(output)):
                groupCounts = {}
                for char in output[i][0]:
                    groupCounts[char] = groupCounts.get(char, 0) + 1
                if currCounts == groupCounts:
                    output[i].append(word)
                    added = True
                    break
            
            if not added:
                output.append([word])

        return output
                