class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # base case:  index is greater than digits
        # decision: 
        # backtracking: remove letter
        
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return
            
            for char in digitToChar[digits[i]]:
                curr += char
                dfs(i + 1, curr)
                curr = curr[:-1]
        
        dfs(0, "")

        return res if len(digits) > 0 else []
