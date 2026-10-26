class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = low + (high - low) // 2
            count = 0
            for n in piles:
                count += math.ceil(float(n) / mid)
            if count <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res