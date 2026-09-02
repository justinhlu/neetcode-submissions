# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1Curr = l1
        l1Arr = []
        while l1Curr:
            l1Arr.append(l1Curr.val)
            l1Curr = l1Curr.next
        
        l1Num = int("".join(map(str, l1Arr[::-1])))

        l2Curr = l2
        l2Arr = []
        while l2Curr:
            l2Arr.append(l2Curr.val)
            l2Curr = l2Curr.next
        
        l2Num = int("".join(map(str, l2Arr[::-1])))

        sumNum = l1Num + l2Num

        stack = []
        for c in str(sumNum):
            stack.append(c)
        
        dummy = res = ListNode(stack.pop())

        while stack:
            res.next = ListNode(stack.pop())
            res = res.next
        
        return dummy
        
        
        
        
