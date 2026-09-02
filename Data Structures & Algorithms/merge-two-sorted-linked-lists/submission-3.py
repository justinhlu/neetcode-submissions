# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        elif list2 is None:
            return list1
        elif list1 is None:
            return list2

        dummy = ListNode()
        currNode = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next

        if list1:
            currNode.next = list1
        if list2:
            currNode.next = list2
        
        return dummy.next

