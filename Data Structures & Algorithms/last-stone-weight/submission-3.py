class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, -(y - x))
            elif x > y:
                heapq.heappush(maxHeap, -(x - y))
            
        if len(maxHeap) == 1:
            return -maxHeap[0]
        else:
            return 0