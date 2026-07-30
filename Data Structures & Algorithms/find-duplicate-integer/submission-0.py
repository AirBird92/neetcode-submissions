class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = [0] * (len(nums) + 1)
        for n in nums:
            if counts[n] > 0:
                return n
            counts[n] += 1
        return -1