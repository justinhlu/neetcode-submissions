class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x2,y2 in points:
            dst = math.sqrt(math.pow(abs(0-x2),2) + math.pow(abs(0-y2),2))
            heapq.heappush(minHeap, [dst, [x2,y2]])
        
        count = 0
        while minHeap and count < k:
            res.append(heapq.heappop(minHeap)[1])
            count += 1

        return res
            