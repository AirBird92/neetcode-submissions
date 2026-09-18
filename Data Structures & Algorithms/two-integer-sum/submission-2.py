class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse_index = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in reverse_index:
                return [reverse_index[diff], i]
            reverse_index[nums[i]] = i