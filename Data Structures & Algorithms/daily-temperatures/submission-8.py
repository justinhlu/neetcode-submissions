class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1][0]] < temperatures[i]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append((i, temperatures[i]))

        return res
            
        
            
