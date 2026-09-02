class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        res = heapq.nsmallest(k, maxHeap)
        print(res)
        return res[-1] * -1

