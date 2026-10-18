class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 1
        maxHeap = []
        heapq.heapify(maxHeap)
        
        for num in nums:
            heapq.heappush(maxHeap, -num)

        while count <= k:
            cur = heapq.heappop(maxHeap)
            if count == k:
                return -1 * cur
            count += 1

        return -1