class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high

        while low <= high:
            mid = low + (high - low) // 2
            total_days, total_weight = 1, 0
            for w in weights:
                if total_weight + w > mid:
                    total_weight = w
                    total_days += 1
                else:
                    total_weight += w
            if total_days <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res