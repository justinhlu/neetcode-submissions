class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        pow = abs(n)
        res = 1
        while pow:
            if pow & 1:
                res *= x
            x *= x
            pow >>= 1
        
        return res if n > 0 else 1 / res