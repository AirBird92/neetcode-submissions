class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                subset = res[j]
                if subset:
                    copy = subset.copy()
                    copy.append(nums[i])
                    res.append(copy)
                else:
                    res.append([nums[i]])
        return res