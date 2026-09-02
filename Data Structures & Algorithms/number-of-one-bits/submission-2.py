class Solution:
    def hammingWeight(self, n: int) -> int:
        bitmask = 1
        count = 0

        for i in range(32):
            if n & bitmask:
                count += 1
            n = n >> 1
        
        return count