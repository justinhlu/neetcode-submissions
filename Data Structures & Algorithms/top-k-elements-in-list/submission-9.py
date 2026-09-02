class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        countMap = {}

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        for key in countMap.keys():
            heapq.heappush(heap,(-countMap[key],key))

        res = []

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res
        
