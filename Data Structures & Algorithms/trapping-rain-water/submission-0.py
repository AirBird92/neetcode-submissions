class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0
        while left <= right:
            if leftMax <= rightMax:
                if height[left] < leftMax:
                    res += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    res += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return res