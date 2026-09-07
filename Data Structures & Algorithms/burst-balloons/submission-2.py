class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded = [1] + nums + [1]
        N = len(padded)
        dp = [[-1] * N for _ in range(N)]
        def dfs(left, right):
            if left == right:
                return 0
            if dp[left][right] >= 0:
                return dp[left][right]
            max_coins = 0
            for i in range(left + 1, right):
                cur = padded[left] * padded[i] * padded[right]
                cur += dp[left][i] if dp[left][i] >= 0 else dfs(left, i)
                cur += dp[i][right] if dp[i][right] >= 0 else dfs(i, right)
                max_coins = max(max_coins, cur)
            dp[left][right] = max_coins
            return max_coins
        return dfs(0, N - 1)