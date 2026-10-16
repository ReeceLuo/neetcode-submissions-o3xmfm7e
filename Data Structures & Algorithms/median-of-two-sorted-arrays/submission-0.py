class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # first thought - combine and sort
        # log (m + n) - indicates binary search

        A, B = nums1, nums2                 # A is smaller array
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B, = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2        # A
            j = half - i - 2        # B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # check if partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                leftMax = max(Aleft, Bleft)
                rightMin = min(Aright, Bright)
                if total % 2 == 0:
                    return (leftMax + rightMin) / 2
                return rightMin
            elif Aleft > Bright:
                r = i - 1
            else: # Bleft > Aright
                l = i + 1
