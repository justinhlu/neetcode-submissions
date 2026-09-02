class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distanceHeap = []
        heapq.heapify(distanceHeap)
        for point in points:
            distance = math.sqrt((math.pow(0 - point[0],2) + math.pow(0-point[1],2)))
            heapq.heappush(distanceHeap, [distance, point])
        
        for i in range(k):
            res.append(heapq.heappop(distanceHeap)[1])
        return res
