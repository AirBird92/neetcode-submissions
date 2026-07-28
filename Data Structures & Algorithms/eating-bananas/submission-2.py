class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) < 2:
            return (piles[0] - 1) // h + 1
        left, right = 1, max(piles)
        minRate = right
        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for n in piles:
                count += math.ceil(n / mid)
            print(count)
            if count <= h:
                minRate = mid
                right = mid - 1
            else:
                left = mid + 1
        return int(minRate)