class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c, = len(matrix), len(matrix[0])
        low, high = 0, r - 1
        left, right = 0, c - 1
        while low <= high:
            mid_row = low + (high - low) // 2
            if matrix[mid_row][left] <= target <= matrix[mid_row][right]:
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[mid_row][mid] == target:
                        return True
                    if matrix[mid_row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            if matrix[mid_row][left] > target:
                high = mid_row - 1
            else:
                low = mid_row + 1
        return False