class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for subAmount in range(1, amount + 1):
            for coin in coins:
                if subAmount - coin >= 0:
                    dp[subAmount] = min(dp[subAmount], 1 + dp[subAmount - coin])
        return dp[amount] if dp[amount] <= amount else -1