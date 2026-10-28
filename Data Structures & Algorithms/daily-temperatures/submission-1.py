class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                prev_temp, prev_pos = stack.pop()
                res[prev_pos] = i - prev_pos
            stack.append((temperatures[i], i))
        return res