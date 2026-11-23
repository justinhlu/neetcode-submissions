class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        q = collections.deque()
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        while maxHeap or q:
            t += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            else:
                t = q[0][1]
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return t