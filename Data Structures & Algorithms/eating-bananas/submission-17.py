class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l+r) // 2
            pileTime = 0
            for pile in piles:
                pileTime += math.ceil(pile/k) 
            
            if pileTime > h:
                # Spent too long eating bananas - need to increase k
                l = k+1
            else:
                res = min(res, k)
                r = k-1
        
        return res