class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x2, y2 in points:
            distance = math.sqrt(math.pow(abs(0 - x2),2) + math.pow(abs(0 - y2), 2))
            heapq.heappush(minHeap, [distance, (x2, y2)])
        
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res
