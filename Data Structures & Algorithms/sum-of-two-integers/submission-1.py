class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while (b != 0):
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask
        
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)

