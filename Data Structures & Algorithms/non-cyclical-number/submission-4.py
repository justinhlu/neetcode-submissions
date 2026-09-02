class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()

        def helper(n):
            stringNum = str(n)
            currSum = 0
            for c in stringNum:
                currSum += pow(int(c), 2)
            
            return currSum
        
        currNum = n
        while currNum != 1:
            currNum = helper(currNum)
            if currNum in numSet:
                return False
            numSet.add(currNum)

        return True