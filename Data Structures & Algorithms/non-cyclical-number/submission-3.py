class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n):
            num = str(n)
            res = 0

            for c in num:
                res += pow(int(c), 2)
            
            return res
        numSet = set()
        while True:
            n = squareSum(n)

            if n == 1:
                return True
            
            if n in numSet:
                return False
            
            numSet.add(n)
        
        return False
