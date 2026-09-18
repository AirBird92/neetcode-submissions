class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        n = len(nums)
        for i in range(n):
            prefix.append(prefix[-1] * nums[i])
        suffix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i + 1])
        return res