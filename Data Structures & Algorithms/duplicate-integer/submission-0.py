class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False