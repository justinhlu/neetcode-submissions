# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        dummy = ListNode(0)
        if list1.val < list2.val:
            dummy.next = list1
            list1 = list1.next
        else:
            dummy.next = list2
            list2 = list2.next

        cur = dummy.next

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next
        
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        
        return dummy.next
