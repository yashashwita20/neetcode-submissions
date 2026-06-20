class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1

        max_vol = 0

        while left < right:
            vol = min(heights[left], heights[right]) * (right - left)

            max_vol = max(max_vol, vol)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_vol