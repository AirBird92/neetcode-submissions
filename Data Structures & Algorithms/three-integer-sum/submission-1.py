class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res_set = set()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res = [nums[i], nums[left], nums[right]]
                    res.sort()
                    res_set.add(tuple(res))
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return list(res_set)