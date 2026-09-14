class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case - stop when len(string) == 2n
        # choice - add left or right parentheses
        # constraint - at any point, cannot be more right than left
            # and num left must equal num right at end
        # backtracking - remove and move on

        res = []

        def dfs(curr, leftCount, rightCount):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            if leftCount < n:
                curr += "("
                dfs(curr, leftCount + 1, rightCount)
                curr = curr[:-1]
            
            if rightCount < leftCount:
                curr += ")"
                dfs(curr, leftCount, rightCount + 1)


        dfs("", 0, 0)
        return res
            