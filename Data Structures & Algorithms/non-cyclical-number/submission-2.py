class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def squareSum(n):
            num = str(n)
            res = 0
            for digit in num:
                res += pow(int(digit), 2)
            return res

        
        while True:
            n = squareSum(n)
            if n == 1:
                return True
            elif n in visit:
                return False
            else:
                visit.add(n)
        
        
