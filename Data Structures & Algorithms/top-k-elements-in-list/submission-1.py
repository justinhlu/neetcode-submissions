class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        
        pq = [(-f, c) for c, f in freqMap.items()]
        heapq.heapify(pq)
        result = []
        for i in range(k):
            f, c = heapq.heappop(pq)
            result.append(c)
        return result
        