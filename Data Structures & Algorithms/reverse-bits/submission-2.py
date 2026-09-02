class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            tmp = ((n >> i)) & 1
            if tmp == 1:
                res |= (1 << 31-i) 
        
        return res