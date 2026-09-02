class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, a in enumerate(temperatures):
            while stack and stack[-1][1] < a:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append([i, a])
        
        return res