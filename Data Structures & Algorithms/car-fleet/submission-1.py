class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = [(p, s) for p, s in zip(position, speed)]
        positionSpeed.sort(reverse=True)
        stack = []
        for p, s in positionSpeed:
            timeToTarget = (target - p) / s
            if not stack or timeToTarget > stack[-1]:
                stack.append(timeToTarget)
        return len(stack)