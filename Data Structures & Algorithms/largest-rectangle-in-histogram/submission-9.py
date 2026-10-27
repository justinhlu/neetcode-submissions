class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0  and stack[-1][1] > h:
                stackInd, stackH = stack.pop()
                area = (i-stackInd) * stackH
                res = max(res, area) 
                start = stackInd

            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            res = max(res, (len(heights)-i) * h)

        return res