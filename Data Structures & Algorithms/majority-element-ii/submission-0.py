class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        freqs = defaultdict(int)
        res = []
        for n in nums:
            freqs[n] += 1
        for n, f in freqs.items():
            if f > N // 3:
                res.append(n)
        return res