class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        cache = [nums[0], nums[1], max(nums[1], nums[0] + nums[2])]
        for i in range(3, n):
            temp = nums[i] + max(cache[0], cache[1])
            cache[0] = cache[1]
            cache[1] = cache[2]
            cache[2] = max(cache[2], temp)
        return cache[2]