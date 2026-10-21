class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq > x:
                high = mid - 1
            else:
                low = mid + 1
                res = mid
        return res