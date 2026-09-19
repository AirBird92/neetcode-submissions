class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        num_set = set(nums)
        res = 0
        for n in num_set:
            if n - 1 not in num_set:
                l = 0
                while n in num_set:
                    l += 1
                    n += 1
                res = max(res, l)
        return res