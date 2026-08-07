class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0, 0]
        for i in range(2, n):
            temp = min(cache[0] + cost[i - 2], cache[1] + cost[i - 1])
            cache[0] = cache[1]
            cache[1] = temp
            print(cache)
        return min(cache[0] + cost[n - 2], cache[1] + cost[n - 1])