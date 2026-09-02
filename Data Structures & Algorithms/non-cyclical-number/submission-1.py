class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def squareSum(n):
            num = str(n)
            res = 0
            for digit in num:
                res += pow(int(digit), 2)
            return res

        
        while n not in visit:
            visit.add(n)
            n = squareSum(n)
            if n == 1:
                return True

        return False
            
        

