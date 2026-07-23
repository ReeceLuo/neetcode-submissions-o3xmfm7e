class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # all combinations -> explore every option -> backtracking

        # base case: stop exploring when string length == 2n
        # decision: add left or right parentheses
        # constraint: right can never be more than left
        # backtracking: remove

        res = []

        def dfs(curr, numLeft, numRight):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if numLeft < n:
                curr += "("
                dfs(curr, numLeft + 1, numRight)
                curr = curr[:-1]

            if numRight < numLeft:
                curr += ")"
                dfs(curr, numLeft, numRight + 1)
        
        dfs("", 0, 0)
        return res