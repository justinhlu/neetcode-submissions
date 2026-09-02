class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = nums
        heapq.heapify(self.maxHeap)
        self.kTh = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)

        return heapq.nlargest(self.kTh,self.maxHeap)[-1]

