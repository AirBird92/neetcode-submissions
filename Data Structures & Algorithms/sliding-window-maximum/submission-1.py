class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return [max(nums)]

        heap = []
        res = []
        left = right = 0
        while right < k:
            heapq.heappush(heap, (-nums[right], right))
            right += 1
        res.append(-heap[0][0])
        while right < len(nums):
            heapq.heappush(heap, (-nums[right], right))
            left += 1
            while heap[0][1] < left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            right += 1
        return res