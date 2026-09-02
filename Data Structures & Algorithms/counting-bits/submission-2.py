class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            bitmask = 1
            for j in range(32):
                if i & bitmask:
                    count += 1
                bitmask <<= 1

            res.append(count)

        return res