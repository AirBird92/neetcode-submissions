class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)

        dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
        for i in range(L1):
            dp[i][L2] = L1 - i
        for j in range(L2):
            dp[L1][j] = L2 - j

        for i in range(L1 - 1, -1, -1):
            for j in range(L2 - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1]
                if word1[i] != word2[j]:
                    dp[i][j] = 1 + min(dp[i][j], dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]