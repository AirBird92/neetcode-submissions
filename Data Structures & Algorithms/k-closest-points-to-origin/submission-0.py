class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [[x, y] for u, (x, y) in heap]
        return res