# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode
        
        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            second.next = tmp1
            first.next = second
            first, second = tmp1, tmp2
        