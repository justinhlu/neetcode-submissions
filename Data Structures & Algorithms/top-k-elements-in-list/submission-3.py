class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] += 1
            else:
                freqMap[nums[i]] = 1
        pq = []
        for n, f in freqMap.items():
            pq.append([-f, n])

        heapq.heapify(pq)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res
        