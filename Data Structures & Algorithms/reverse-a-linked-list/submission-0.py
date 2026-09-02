# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prev = None

        while currNode:
            nextNode = currNode.next #2
            currNode.next = prev #0
            prev = currNode #1
            currNode = nextNode #2
        
        return prev
