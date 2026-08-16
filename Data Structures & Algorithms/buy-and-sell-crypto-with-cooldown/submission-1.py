class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            # If I'm buying
            # choose to buy
            buy = dp[i - 2][False] - prices[i] if i - 2 >= 0 else -prices[i]
            # choose not to buy
            skip = dp[i - 1][True] if i - 1 >= 0 else float('-inf')
            dp[i][True] = max(buy, skip)

            # If I'm selling
            # choose to sell
            sell = dp[i - 1][True] + prices[i] if i - 1 >= 0 else float('-inf')
            # choose not to sell
            skip = dp[i - 1][False] if i - 1 >= 0 else 0
            dp[i][False] = max(sell, skip)
        return dp[-1][False]