class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(i, j, prev, reached):
             queue = deque([(i, j, prev)])
             while queue:
                l = len(queue)
                for _ in range(l):
                    x, y, prev = queue.popleft()
                    if x in range(rows) and y in range(cols) and (x, y) not in reached and heights[x][y] >= prev:
                        reached.add((x, y))
                        for dx, dy in directions:
                            queue.append((x + dx, y + dy, heights[x][y]))
        pacific = set()
        for i in range(rows):
            bfs(i, 0, 0, pacific)
        for j in range(cols):
            bfs(0, j, 0, pacific)
        atlantic = set()
        for i in range(rows):
            bfs(i, cols - 1, 0, atlantic)
        for j in range(cols):
            bfs(rows - 1, j, 0, atlantic)
        return list(pacific.intersection(atlantic))