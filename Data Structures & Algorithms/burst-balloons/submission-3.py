class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded = [1] + nums + [1]
        N = len(padded)
        dp = [[0] * N for _ in range(N)]

        for width in range(0, N):
            for left in range(0, N - width):
                right = left + width
                for i in range(left + 1, right):
                    cur = padded[left] * padded[i] * padded[right] + dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], cur)
        return dp[0][N - 1]