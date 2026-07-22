class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefixProd = [1] * l
        for i in range(1, l):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]
        suffixProd = [1] * l
        for i in range(l - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i + 1]
        res = [0] * l
        for i in range(l):
            res[i] = prefixProd[i] * suffixProd[i]
        return res