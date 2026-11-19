class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, curr):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            if left < n:
                curr += "("
                dfs(left + 1, right, curr)
                curr = curr[:-1]
            
            if right < left:
                curr += ")"
                dfs(left, right + 1, curr)
                
        dfs(0, 0, "")
        return res
        
