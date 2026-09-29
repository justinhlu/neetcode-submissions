class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        res = []

        for x1, y1 in points:
            distance = math.sqrt(math.pow(0 - x1, 2) + math.pow(0 - y1, 2))
            heapq.heappush(minHeap, [distance, [x1,y1]])
        
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res
