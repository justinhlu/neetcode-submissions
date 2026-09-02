class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            bitmask = 1 << i
            if n & bitmask:
                res += 1
        return res
            