class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all indice triplets 
        # brute force - take every indice pair and scan along for third
        # indice. O(n^3) solution because we need to scan O(n) times for
        # O(n^2) pairs.
        # better. sort and do sorted two sum method

        # notes:
        # when we increment i, we want to make sure we're getting a new
        # number than before. 
            # this is because at each i, we fully explore the range
            # of values i [l ... r].
            # if we increment i and get the same number, we're exploring
            # a range of numbers ALREADY COVERED by the previous range.
        
        # when we fully explore the range [l ... r] by incrementing l or r,
        # make sure at least one of them is not the same as their prev value
        # because it could be the case that there are duplicates.
            # for example: -1 [0, 0, 1, 1]
            # changing one value will offset other to prevent duplicatse


        nums.sort()

        res = []
        i = 0
        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    k = l + 1
                    while k < r and nums[k] == nums[l]:
                        k += 1
                    l = k

            j = i + 1
            while j < len(nums) - 2 and nums[j] == nums[i]:
                j += 1
            i = j
        
        return res

        # [-4, -1, -1, 0, 1, 2]