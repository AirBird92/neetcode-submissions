class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        for pos, sp in cars:
            time = (target - pos) / sp
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)