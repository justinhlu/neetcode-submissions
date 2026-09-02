# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1
        
        if group == k:
            curr = head
            prev = self.reverseKGroup(cur, k)
            while group > 0: # Reverse nodes until group is 0
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                group -= 1
            head = prev
        return head