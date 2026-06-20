class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        stack = [] 

        for i, bar in enumerate(height):
            while stack and bar >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    h = min(left, bar) - mid
                    w = i - stack[-1] - 1
                    water += h * w
            stack.append(i)

        return water
        