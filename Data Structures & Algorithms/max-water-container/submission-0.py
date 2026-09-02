class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j - i
                area = min(heights[i], heights[j]) * width
                maxArea = max(area, maxArea)
        
        return maxArea