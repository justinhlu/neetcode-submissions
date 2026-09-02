class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if stack and temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    res[index] = i - index
                stack.append(i)
                
            else:
                stack.append(i)

        return res