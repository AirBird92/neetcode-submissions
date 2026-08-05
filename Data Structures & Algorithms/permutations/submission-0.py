class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False for _ in nums]
        def dfs(permutation):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    permutation.append(nums[i])
                    dfs(permutation)
                    permutation.pop()
                    picked[i] = False
        dfs([])
        return res