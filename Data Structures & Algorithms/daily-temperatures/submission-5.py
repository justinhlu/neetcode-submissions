class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 

        for i in range(len(temperatures)):
            if stack and temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        
        return res