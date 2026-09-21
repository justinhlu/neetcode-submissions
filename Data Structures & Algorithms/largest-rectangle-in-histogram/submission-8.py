class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i 

            while len(stack) > 0 and stack[-1][1] > h:
                stackInd, stackH = stack.pop()
                area = stackH * (i-stackInd)
                maxArea = max(maxArea, area)
                start = stackInd
            
            stack.append((start, heights[i]))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights)-i) * h)

        return maxArea