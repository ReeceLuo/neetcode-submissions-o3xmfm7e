class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # base case - if index is longer than string
        # decision - when creating substrings, how long do we want
        # to make them?
            # ex: aab
            # first substring can be a, aa, or aab
            # however, not all are palindromes, and we only split
            # if palindrome

            # if palindrome, split off and find palindromes within
            # rest of string
        # 

        res = []
        curr = []

        def checkPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return
        
            for j in range(i, len(s)):
                if checkPalindrome(s, i, j):
                    curr.append(s[i : j + 1])
                    dfs(j + 1)
                    curr.pop()

        dfs(0)
        return res



