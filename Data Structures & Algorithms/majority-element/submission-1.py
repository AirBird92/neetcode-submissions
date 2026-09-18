class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
            if freqs[n] > N // 2:
                return n