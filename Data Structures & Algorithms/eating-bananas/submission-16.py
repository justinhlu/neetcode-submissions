class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            pileTime = 0
            k = (l + r) // 2
            for pile in piles:
                pileTime += math.ceil(pile / k)
            
            if pileTime > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

        return res