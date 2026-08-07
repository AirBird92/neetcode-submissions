class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        cache = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            temp = max(cache[1], cache[0] + nums[i])
            cache[0] = cache[1]
            cache[1] = temp
        return cache[1]