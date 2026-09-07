class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)

        dp = [0] * (L2 + 1)
        next_dp = [0] * (L2 + 1)

        for j in range(L2 + 1):
            dp[j] = L2 - j

        for i in range(L1 - 1, -1, -1):
            next_dp[L2] = L1 - i
            for j in range(L2 - 1, -1, -1):
                next_dp[j] = dp[j + 1]
                if word1[i] != word2[j]:
                    next_dp[j] = 1 + min(next_dp[j], dp[j], next_dp[j + 1])
            dp = next_dp[:]
        return dp[0]