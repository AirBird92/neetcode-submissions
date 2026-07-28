class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(row: List[int], target: int) -> bool:
            if len(row) < 2:
                return row[0] == target
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < row[mid]:
                    right = mid - 1
                elif target > row[mid]:
                    left = mid + 1
                else:
                    return True
            return False
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                top = mid + 1
            else:
                return searchRow(matrix[mid], target)
        return False