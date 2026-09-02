# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return False

        hasCycle = False
        slow = head
        fast = head

        while fast != None and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                hasCycle = True
                break

        return hasCycle