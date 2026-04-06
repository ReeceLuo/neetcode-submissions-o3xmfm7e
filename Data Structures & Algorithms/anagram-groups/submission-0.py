class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # must check letter counts with others
        # brute force - check letter counts with first word
        # of each group, append to list if same, make new list if diff

        output = []
        for word in strs:
            currCount = {}
            for char in word:
                currCount[char] = currCount.get(char, 0) + 1

            found = False
            for i, group in enumerate(output):
                member = group[0]
                memberCount = {}
                for char in member:
                    memberCount[char] = memberCount.get(char, 0) + 1

                if currCount == memberCount:
                    output[i].append(word)
                    found = True

            if not found:
                output.append([word])

        return output