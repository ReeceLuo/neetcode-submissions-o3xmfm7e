class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # base case - if index is longer than string
        # decision - add a letter to current substring or create new
        # 

        res = []

        def checkPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(j, i, curr):
            if i >= len(s):
                if i == j:
                    res.append(curr.copy())
                return
            
            if checkPalindrome(s, j, i):
                curr.append(s[j : i + 1])
                dfs(i + 1, i + 1, curr)
                curr.pop()
            
            dfs(j, i + 1, curr)
        
        dfs(0, 0, [])
        return res








