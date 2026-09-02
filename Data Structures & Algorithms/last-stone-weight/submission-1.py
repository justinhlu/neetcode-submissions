class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            if stone1 < stone2:
                newStone = stone2 - stone1
                heapq.heappush(maxHeap, -newStone)
            elif stone1 > stone2:
                newStone = stone1 - stone2
                heapq.heappush(maxHeap, -newStone)
        
        if len(maxHeap) == 1:
            return abs(maxHeap[0])
        else:
            return 0