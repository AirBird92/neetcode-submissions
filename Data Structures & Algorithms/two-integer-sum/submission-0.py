class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverseIndex = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            j = reverseIndex.get(diff)
            if j is not None:
                return [j, i]
            reverseIndex[nums[i]] = i
        return [-1, -1]
