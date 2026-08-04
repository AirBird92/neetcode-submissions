class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq, offset = [0] * 26, ord('A')
        for c in tasks:
            freq[ord(c) - offset] += 1
        heap = [-f for f in freq if f > 0]
        heapq.heapify(heap)
        queue, time = deque(), 0
        while heap or queue:
            time += 1
            if heap:
                cur = 1 + heapq.heappop(heap)
                if cur < 0:
                    queue.append((cur, time + n))
            else:
                time = queue[0][1]
            if queue and queue[0][1] == time:
                cur = queue.popleft()
                heapq.heappush(heap, cur[0])
        return time