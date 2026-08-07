class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1, 1]
        for _ in range(1, n):
            s = sum(mem)
            mem[0] = mem[1]
            mem[1] = s
            print(mem)
        return mem[1]