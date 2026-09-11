class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # base case
        # choice
        # constraint
        # backtracking solution

        # return list of all unique combinations of candidates whose chosen numbers sum to target
        # must NOT contain duplicate

        res = []
        candidates.sort()

        def dfs(i, currSum, curr):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, currSum + candidates[i], curr)

            curr.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, currSum, curr)

        
        dfs(0, 0, [])
        return res


