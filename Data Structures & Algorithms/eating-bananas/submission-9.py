class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

       
        while l <= r:
            kTh = (l+r) // 2
            pileTime = 0
            for pile in piles:
                pileTime += math.ceil(pile / kTh)
            
            if pileTime > h:
                l = kTh + 1
        
            else:
                r = kTh - 1
                res = min(res, kTh)
        
        return res
        
                