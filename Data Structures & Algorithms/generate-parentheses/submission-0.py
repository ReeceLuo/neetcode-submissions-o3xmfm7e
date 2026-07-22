class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        # base case - when length of string == 2n
        # decision - whether to add left or right parentheses
        # constraint - can never be more riht than left

        res = []

        def dfs(curr, numLeft, numRight):
            if numRight > numLeft or numLeft > n:
                return
            if len(curr) == n * 2:
                res.append(curr)
                return
            
            curr += "("
            dfs(curr, numLeft + 1, numRight)

            curr = curr[:-1]
            curr += ")"
            dfs(curr, numLeft, numRight + 1)

        dfs("", 0, 0)

        return res
        

