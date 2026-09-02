class Solution:
    def reverseBits(self, n: int) -> int:
        res = [0] * 32
        for i in range(32):
            bitmask = 1 << i
            if n & bitmask:
                res[i] = 1

        res = int("".join(map(str, res)), 2)
        return res