class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        i = 1
        while i < k and maxHeap:
            heapq.heappop(maxHeap)
            i += 1

        return -1 * heapq.heappop(maxHeap) if maxHeap else -1
