class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        res = r
        l = 1

        while l <= r:
            kTh = (l + r) // 2
            currTime = 0

            for pile in piles:
                currTime += math.ceil(pile / kTh)
            
            if currTime > h:
                l = kTh + 1
            else:
                r = kTh - 1
                res = min(res, kTh)

        return res