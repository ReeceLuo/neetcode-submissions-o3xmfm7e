class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking:
        # base case
        # choices (decision tree)
        # constraints
        # backtracking action

        # choice: include or dont include 
        res = []

        # recursive dfs algorithm
        # base case - when current sum equals target
        # when i >= len(nums) or current sum greater than target

        # group duplicates together and skip to next number if exlcuding
        candidates.sort()

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])
            curr.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, curr, currSum)
        
        dfs(0, [], 0)
        return res

