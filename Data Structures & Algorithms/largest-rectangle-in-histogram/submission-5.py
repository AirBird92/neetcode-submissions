class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return heights[0]
        stack = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            prev = None
            while stack and heights[i] <= stack[-1][0]:
                res = max(res, (i - stack[-1][1]) * stack[-1][0])
                prev = stack.pop()
            stack.append((heights[i], i if prev is None else prev[1]))
        return res