class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            for j in range(32):
                bitmask = 1 << j
                
                if i & bitmask:
                    count += 1
            res.append(count)
        return res