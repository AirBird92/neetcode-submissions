class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if s1 != s2:
                heapq.heappush(heap, -abs(s1 - s2))
        return -heap[0] if heap else 0