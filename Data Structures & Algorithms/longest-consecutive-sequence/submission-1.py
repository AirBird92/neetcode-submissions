class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        i, j = 0, 1
        longest = 0
        curLen = 1
        while j < len(nums):
            if nums[j] == nums[j - 1]:
                j += 1
            elif nums[j] - nums[j - 1] == 1:
                curLen += 1
                j += 1
            else:
                longest = max(longest, curLen)
                curLen = 1
                i = j
                j += 1
        return max(longest, curLen)
            