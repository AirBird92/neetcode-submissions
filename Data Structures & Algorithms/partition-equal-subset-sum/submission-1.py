class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        sumsSoFar = set()
        for n in nums:
            if n == target:
                return True
            for s in list(sumsSoFar):
                if n + s == target:
                    return True
                sumsSoFar.add(n + s)
            sumsSoFar.add(n)
        return False