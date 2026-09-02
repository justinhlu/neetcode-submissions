# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        second = dummy

        for i in range(n):
            curr = curr.next
        
        while curr != None:
            curr = curr.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next