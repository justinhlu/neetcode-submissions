class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minPileTime = r
        while l <= r:
            pileTime = 0
            mid = (l + r) // 2
            for pile in piles:
                pileTime += math.ceil(float(pile) / mid)


            if pileTime > h:
                l = mid + 1
            elif pileTime < h:
                minPileTime = min(minPileTime, mid)
                r = mid - 1
            else:
                minPileTime = min(minPileTime, mid)
                r = mid - 1

        return minPileTime