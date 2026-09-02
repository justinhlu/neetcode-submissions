class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        res = []
        freqMap = defaultdict(list)

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        for key in freqMap.keys():
            heapq.heappush(heap, (-freqMap[key], key))

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

        