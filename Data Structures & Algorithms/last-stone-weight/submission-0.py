class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = []
        heapq.heapify(stoneHeap)
        for stone in stones:
            heapq.heappush(stoneHeap, -stone)
        
        while len(stoneHeap) > 1:
            stoneX = heapq.heappop(stoneHeap)
            stoneY = heapq.heappop(stoneHeap)

            if (stoneX != stoneY):
                newWeight = abs(stoneX - stoneY)
                heapq.heappush(stoneHeap, -newWeight)
        
        if len(stoneHeap) == 1:
            return -heapq.heappop(stoneHeap)
        else:
            return 0
