class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                subset = res[j]
                copy = subset.copy()
                copy.append(nums[i])
                res.append(copy)
        return res