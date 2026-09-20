class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            i += 1
            if j < len(nums):
                nums[i] = nums[j]
        return i