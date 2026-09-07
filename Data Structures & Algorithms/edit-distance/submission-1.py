class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)

        dp = [[-1] * (L2 + 1) for _ in range(L1 + 1)]
        def dfs(i, j):
            if i == L1:
                return L2 - j
            if j == L2:
                return L1 - i
            
            dp[i][j] = dp[i + 1][j + 1] if dp[i + 1][j + 1] >= 0 else dfs(i + 1, j + 1)
            if word1[i] == word2[j]:
                return dp[i][j]
            
            dp[i][j] = 1 + min(dp[i][j],
                dp[i][j + 1] if dp[i][j + 1] >= 0 else dfs(i, j + 1), 
                dp[i + 1][j] if dp[i + 1][j] >= 0 else dfs(i + 1, j)
            )
            return dp[i][j]

        return dfs(0, 0)