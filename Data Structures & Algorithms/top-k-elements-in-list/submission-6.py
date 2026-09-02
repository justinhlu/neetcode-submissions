class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        for num in freqMap.keys():
            heapq.heappush(heap, (freqMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res