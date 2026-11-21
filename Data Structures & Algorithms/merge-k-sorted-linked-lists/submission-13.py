# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        minHeap = []
        dummy = cur = ListNode(0)
        counter = 0
        for newList in lists:
            if newList:
                heapq.heappush(minHeap, (newList.val, counter, newList))
                counter += 1
        
        while minHeap:
            val, _, newNode = heapq.heappop(minHeap)

            cur.next = newNode
            if newNode.next:
                heapq.heappush(minHeap, (newNode.next.val, counter, newNode.next))
                counter += 1

            cur = cur.next
        
        return dummy.next
        