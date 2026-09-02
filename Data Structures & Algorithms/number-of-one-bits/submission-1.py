class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            bitmask = 1 << i
            if n & bitmask:
                count += 1
        
        return count