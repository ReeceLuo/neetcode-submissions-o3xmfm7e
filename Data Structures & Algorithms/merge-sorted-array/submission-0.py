class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m: number of valid elements in nums1
        # n: number of elements in nums2

        # brute force - add all elements of nums2 to end of nums1, then
        # sort -> O(nlogn)

        for i in range(n):
            nums1[m + i] = nums2[i]
        
        nums1.sort()