class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[N - 1] = True
        
        for i in range(N - 1, -1, -1):
            if nums[i] == 0:
                continue
            
            end = min(N - 1, i + nums[i])
            for j in range(end, i, -1):
                dp[i] = dp[i] or dp[j]
        
        return dp[0]