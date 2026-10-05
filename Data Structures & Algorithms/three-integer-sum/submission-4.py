class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all indice triplets 
        # brute force - take every indice pair and scan along for third
        # indice. O(n^3) solution because we need to scan O(n) times for
        # O(n^2) pairs.
        # better. sort and do sorted two sum method

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