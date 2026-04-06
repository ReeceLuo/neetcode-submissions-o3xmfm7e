class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force
        # for i in range(0, len(matrix)):
        #     for j in range(0, len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True

        # return False

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = int((left + right) / 2)
            midValue = matrix[mid // len(matrix[0])][mid % len(matrix[0])]

            if midValue == target:
                return True
            elif midValue < target:
                left = mid + 1
            else:
                right = mid - 1

        return False




