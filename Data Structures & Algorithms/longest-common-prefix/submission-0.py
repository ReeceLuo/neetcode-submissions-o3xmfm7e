class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        smallest = strs[0]
        for word in strs:
            if len(word) < len(smallest):
                smallest = word

        for i, char in enumerate(smallest):
            exit = False
            for word in strs:
                if word[i] != char:
                    exit = True
                    break
            if exit:
                break
            prefix += char

        return prefix