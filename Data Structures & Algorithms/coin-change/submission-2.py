class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([0])
        count = 0
        visited = [False] * (amount + 1)
        while queue:
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                if cur == amount:
                    return count
                if cur > amount or visited[cur]:
                    continue
                visited[cur] = True
                for coin in coins:
                    queue.append(cur + coin)
            count += 1
        return -1