class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        total = 0
        def dfs(i):
            nonlocal total
            if total == target:
                res.append(combination.copy())
                return
            if total > target or i >= len(nums):
                return
            combination.append(nums[i])
            total += nums[i]
            dfs(i)
            combination.pop()
            total -= nums[i]
            dfs(i + 1)
        dfs(0)
        return res