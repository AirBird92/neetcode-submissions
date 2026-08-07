class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        def dp(nums, l, r):
            cache = [nums[l], max(nums[l], nums[l + 1])]
            for i in range(l + 2, r):
                temp = max(cache[1], cache[0] + nums[i])
                cache[0] = cache[1]
                cache[1] = temp
            return cache[1]
        
        return max(dp(nums, 0, n - 1), dp(nums, 1, n))