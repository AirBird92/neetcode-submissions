class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums_set = set(nums)
        res = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            cur_len = 1
            while n + cur_len in nums_set:
                cur_len += 1
            res = max(res, cur_len)
        return res