class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            stackInd = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i-index) * height)
                stackInd = index
            
            stack.append([stackInd, h])
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h )
        
        return maxArea

            
            