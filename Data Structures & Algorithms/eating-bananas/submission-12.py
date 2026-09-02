class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            pileTime = 0

            for pile in piles:
                time = math.ceil(pile / k)
                pileTime += time
            
            if pileTime > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

        return res