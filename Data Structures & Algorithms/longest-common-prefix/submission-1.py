class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                word = strs[j]
                if i >= len(word) or word[i] != char:
                    return prefix
            prefix += char

        return prefix
            