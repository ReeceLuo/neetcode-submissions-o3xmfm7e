class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) additional space indicates some scanning solution like
        # two pointer. In normal two sum, we use a dictionary for an 
        # O(n) solution. Here, we can use sorted property
            # start at ends. if smaller than target, increment left.
            # if bigger, increment right. if equal, return
        # Always will be one valid solution
        # one indexed

        l, r = 0, len(numbers) - 1
        
        while l < r:
            res = numbers[l] + numbers[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        return []