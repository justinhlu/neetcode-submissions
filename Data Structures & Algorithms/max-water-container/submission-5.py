class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            maxArea = max(maxArea, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return maxArea