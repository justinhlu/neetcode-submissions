class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            higherTempFound = False
            for j in range(i+1, len(temperatures)):
                count += 1

                if temperatures[j] > temperatures[i]:
                    higherTempFound = True
                    break

            if higherTempFound:
                res.append(count)
            else:
                res.append(0)
    
        return res