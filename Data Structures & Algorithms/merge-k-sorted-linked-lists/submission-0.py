# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for lst in lists:
            while lst:
                res.append(lst.val)
                lst = lst.next
            
        res.sort()

        dummy = curr = ListNode(0)

        for num in res:
            node = ListNode(num)
            curr.next = node
            curr = curr.next

        return dummy.next


        
