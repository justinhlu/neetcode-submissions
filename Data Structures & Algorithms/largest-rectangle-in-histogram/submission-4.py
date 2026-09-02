class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            index = i

            while stack and stack[-1][1] > h:
                stackInd, stackH = stack.pop()
                maxArea = max(maxArea, (i-stackInd) * stackH)
                index = stackInd
            
            stack.append([index, heights[i]])
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)
            
        return maxArea