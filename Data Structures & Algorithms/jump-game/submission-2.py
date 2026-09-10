class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [None] * N
        def dfs(i) -> bool:
            if dp[i] is not None:
                return dp[i]
            if i == N - 1:
                return True
            if nums[i] == 0:
                return False

            end = min(N - 1, i + nums[i])
            for  j in range(end, i, -1):
                if dfs(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False

        return dfs(0)