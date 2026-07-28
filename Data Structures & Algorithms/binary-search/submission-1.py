class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0 if nums[0] == target else -1
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1