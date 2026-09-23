class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, prev = 0, prices[0]
        for i in range(1, len(prices)):
            prev = min(prev, prices[i])
            res = max(res, prices[i] - prev)
        return res